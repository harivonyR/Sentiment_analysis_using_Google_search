# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 21:37:13 2025

@author: HarivonyR

This script will load pre-trained model to predict sentiment score based on the 
provided text (snippets in our case)

Best Practices

+Regularly clean up old models if you test a lot of Transformers.
+Move to a secondary drive if your system SSD is small.
+Avoid unnecessarily re-running from_pretrained as it will re-download if the cache has been cleared.

"""

# step 1. manage space
import os
os.environ["HF_HOME"] = "D:/HuggingFace"

# step 2. optimise ressources
# pip install huggingface_hub[hf_xet]

# step 3. import model
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def get_sentiment_score(text):
    # Tokenize
    encoded_text = tokenizer(text, return_tensors='pt')

    # Get model output (logits)
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Print the sentiment scores
    scores_dict = {
      'roberta_neg': scores[0],
      'roberta_neu': scores[1],
      'roberta_pos': scores[2]
    }
    
    # Calculate the compound score
    scores_dict["compound"] = scores_dict['roberta_pos'] - scores_dict['roberta_neg']

    print(text)
    print(scores_dict)

    return scores_dict


if __name__ == "__main__":
    texte = "I overclocked my toaster once… now it only burns data."
    score = get_sentiment_score(texte)
    # output : {'roberta_neg': 0.7536289, 'roberta_neu': 0.21952808, 'roberta_pos': 0.026842946, 'compound': -0.72678596}
    

#Step 4 : manage your storage by cleaning your cache after execution
#:\Users\<USERNAME>\.cache\huggingface\hub


