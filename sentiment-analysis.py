import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

# 1.Load dataset 
df = pd.read_csv("sample_tweets.csv")

print("Columns in CSV:", df.columns.tolist())

# Rename columns to use later in our code
df = df.rename(columns={'date': 'Date', 'tweet': 'Tweet'})

# 2.Sentiment Analysis 
def get_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

df["Sentiment"] = df["Tweet"].apply(get_sentiment)

# 3.Summary Counts
print("Sentiment Counts:")
print(df["Sentiment"].value_counts())

# Saving results and percentage breakdown
df.to_csv("nvidia_sentiment_results.csv", index=False)
print("Results saved as nvidia_sentiment_results.csv")
sentiment_percent = df["Sentiment"].value_counts(normalize=True) * 100
print("Sentiment Percentage:\n", sentiment_percent)


#4. Visualization: Sentiment Distribution
sns.set(style="darkgrid")
plt.figure(figsize=(6,9))
sns.countplot(x="Sentiment", data=df, palette="Set2")
sns.despine()
plt.title("Overall Sentiment Distribution for Nvidia")
plt.show()

# 5. Visualization: Sentiment Trend over Time 
# Convert Date to proper datetime format
df['Date'] = pd.to_datetime(df['Date'])

#6. Create a date-only column for better visualization
df['Date_only'] = df['Date'].dt.date

plt.figure(figsize=(12,6))
sns.countplot(x="Date_only", hue="Sentiment", data=df, palette="muted")
plt.title("Sentiment Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
