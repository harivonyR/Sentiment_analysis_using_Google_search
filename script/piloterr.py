# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 21:38:24 2025

@author: BEST
"""

from credential import x_api_key
import requests


def scrape_page_results(key_word="NLP", page=1, limit=20,organic_results=True):
    """
    set organic_results=False if a raw response is needed
    
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
    
    print(f"[{key_word}] : page {page} scraped | results {len(response.json().get('organic_results', []))} founds")
    
    if organic_results:
        return response.json().get('organic_results', [])
    
    else :
        return response.json()
    
def get_search_results(key_word="NLP",page_limit=10,result_limit=20):
    results=[]
    for i in range(page_limit):
        response = scrape_page_results(key_word=key_word,page=i,limit=result_limit)
        results.extend(response)
        
    return results

def test():
    """
    Pipeline function test (Optional)
    """
    # Get result of a search in page 1
    #page_results = scrape_page_results(key_word="Trump", page=1, limit=100)
    search_results = get_search_results(key_word="Boing 777",page_limit=20,result_limit=100)

    
if __name__ =="__main__":
    test()
    