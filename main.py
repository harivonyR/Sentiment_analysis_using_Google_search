# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 21:37:47 2025

@author: HarivonyR

This script will take a key word and scrape all result found we Piloterr Google search API

Then transform the output object into dataframe.

Finally, it loop over snippets found to predict and attribute sentiment score for each row.

"""
import pandas as pd
from script.google_search_scraping import get_search_results
from script.util import list_dict_to_df
from script.sentiment_analysis import get_sentiment_score

def get_google_search_sentiment(key_word="Lorem Ipsum",page_limit=10,result_limit=20):
    
    # step 1. scrape the google search result
    search_results = get_search_results(key_word=key_word,page_limit=page_limit,result_limit=result_limit)
    
    # step 2. get the dataframe for analysis
    df_search_results = list_dict_to_df(search_results)
    
    # step 3. loop row and predict sentiment score based on snippet column
    sentiment_scores_series = df_search_results['snippet'].apply(get_sentiment_score)
    
    # step 4. Convert the series of dictionaries into a DataFrame
    sentiment_scores_df = pd.DataFrame(sentiment_scores_series.tolist(), index=df_search_results.index)
    
    # step 5. Concatenate the original DataFrame with the sentiment scores DataFrame
    df_with_sentiment = pd.concat([df_search_results, sentiment_scores_df], axis=1)
    
    return df_with_sentiment

if __name__ == "__main__":
    
    analysis_targer = "Ukraine war site:reddit.com"
    df_results = get_google_search_sentiment(key_word=analysis_targer)