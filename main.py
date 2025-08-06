# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 21:37:47 2025

@author: HarivonyR

This script will take a key word and scrape all result found we Piloterr Google search API

Then transform the output object into dataframe.

Finally, it loop over snippets found to predict and attribute sentiment score for each row.

"""



from script.google_search_scraping import get_search_results
from script.util import list_dict_to_df
from script.sentiment_analysis import get_sentiment_score



search_object = get_search_results(key_word="Donald Trump",page_limit=10,result_limit=20)


