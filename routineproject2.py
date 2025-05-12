# project
# Social Media Sentiment Analysis
# Task: Process a dataset of tweets (columns: TweetID, Text, Likes, Date).
# Requirements:
# Clean text (remove special characters).
# Categorize tweets as "Positive," "Neutral," or "Negative" based on keywords.
# Calculate average likes per sentiment category.
# Plot sentiment distribution in a pie chart.
# Deliverable: Summary of sentiment trends and chart.


import pandas as pd
# import re
import matplotlib.pyplot as plt
from collections import Counter

# Load the dataset (Ensure the CSV file matches column names)
df = pd.read_csv("tweet_sentiment.csv")

# Function to clean text (removes special characters, links, and numbers)
# print(df.isnull())
# print(df.drop_duplicates())
# print(df.dropna())

df1= df.head(51)
# print(df1)
# Categorize sentiment (based on given labels)
df1["Sentiment"] = df1["sentiment"]

# Count sentiment occurrences
sentiment_counts = Counter(df1["Sentiment"])

average_likes=df1['likes'].mean()
print("Average likes: ",average_likes,"likes")

# Plot sentiment distribution in a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct="%1.1f%%", colors=["blue", "red", "green"])
plt.title("Sentiment Distribution of Tweets")
plt.show()

# Print sentiment summary
print("Sentiment Counts:")
print(sentiment_counts)

df1.to_csv('updated_tweet_sentiments.csv')