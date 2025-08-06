# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 21:40:35 2025

@author: BEST
"""

import pandas as pd

def list_dict_to_df(data):

    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise ValueError("L'entrée doit être une liste de dictionnaires.")

    df = pd.DataFrame(data)
    return df