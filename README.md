# Sentiment Analysis Using Google Search

Google Search results scraper combined with NLP-based sentiment analysis using the **Piloterr Google Search API**.

This project focuses on:
- Extracting real-time search results from Google
- Calculating sentiment scores (negative, neutral, positive, compound) for each snippet
- Preparing structured data for further visualization or reporting *(visualization is **not** included in this repo)*

---

## Clone the project
```bash
git clone https://github.com/harivonyR/Sentiment_analysis_using_Google_search/
cd Sentiment_analysis_using_Google_search
```

---

## Configure your API key
Edit the credentials file:
```bash
cd credential.example
nano credential.py
```
Replace the placeholder with your **Piloterr API Key**.  
You can request a key from [Piloterr.com](https://piloterr.com).

---

## Install dependencies
**Core (development)**:
```bash
pip install pandas requests os
```

**NLP Models**:
```bash
pip install scipy transformers torch
```

---

## Run the main script
```bash
python main.py
```
This will:
1. Scrape Google search results for your chosen keyword
2. Calculate sentiment scores for each row in the dataset
3. Return the results as dataframe for your own analysis and visualization

---

💡 *Explore the full analysis with data visualisation on [Google Colab : Sentiment analysis using Piloterr Google Search API and NLP.](https://colab.research.google.com/drive/1-QSPNH3HITs6MeJd5FFzMlpM1GZzOuTU#scrollTo=wByn7X91YLDz)