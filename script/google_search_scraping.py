# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 21:38:24 2025

@author: HarivonyR

Use : This script will help retrieving result of google search using piloterr API
Output ; List object of the result with title, link, and snippets

"""

from credential import x_api_key
import requests


def google_search(key_word="NLP", page=1, limit=20):
    """
    this function will return the google search result found with the inputed keyword
    """
    url = "https://piloterr.com/api/v2/google/search"

    payload = {
        "query": str(key_word),
        "page": page,          # page define the page numbering
        "num" : limit          # limit define the number of result to scrape in the result page
    }
    headers = {
        "x-api-key": x_api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    organic_result = response.json().get('organic_results', [])
    print(f"[{key_word}] : page {page} scraped | {len(organic_result)} results found")
    return organic_result

def get_search_results(key_word="NLP",page_limit=10,result_limit=20):
    """
    this function will loop fetching result in each google result page
    """
    results=[]
    for i in range(page_limit):
        response = google_search(key_word=key_word,page=i,limit=result_limit)
        results.extend(response)
    return results


if __name__ =="__main__":
    """
    Pipeline function test (Optional)
    """
    # Get result of a search in page 1
    page_results = get_search_results(key_word="Trump", page_limit=1, limit=100)
    dict_results = get_search_results(key_word="Bitcoin -inurl:youtube.com",page_limit=4,result_limit=100)

    