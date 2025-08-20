# TecHorizon Sentiment Tracker

A Python-based sentiment analysis tool for tracking brand sentiment on X. Built for the 2025 TechHorizon internship. Pandas are used for data handling, TextBlob for sentiment analysis, and Seaborn for visualization. For this repository, I created a sample csv tweets file on people's sentiment towards NVIDIA.

## Features

- Analyze tweets from a CSV dataset (`sample_tweets.csv`)
- Sentiment classification: Positive 😊, Negative 😠, Neutral 😐
- View overall sentiment distribution
- Track sentiment trends over time
- Export analysis results to CSV

## Results

The project generates two key visualizations:

1. **Overall Sentiment Distribution** → shows the percentage of positive, negative, and neutral tweets.
2. **Sentiment Trend Over Time** → shows how sentiment changes across different dates.

## How to Run Locally

```bash
pip install -r requirements.txt
python sentiment_analysis.py
