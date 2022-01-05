from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_anorexia_snippets.csv')
df2 = df.sort_values(by='year', ascending=True)
df2['Snippet'] = df2['Snippet'].apply(str)

analyzer = SentimentIntensityAnalyzer()
df2['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df2['Snippet']]
df2['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df2['Snippet']]
df2['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df2['fullText']]
df2['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df2['Snippet']]


sns.lineplot(x="year", y="compound", data=df2, color='black')
sns.set_theme(style="darkgrid")
plt.xlabel('Year of Publication')
plt.ylabel('Polarity')
plt.title('Sentiment of "anorexia" in $\it{The\ Lancet}$ corpus')

plt.show()