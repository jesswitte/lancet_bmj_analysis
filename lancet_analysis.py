import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
import re as re
from textblob.sentiments import NaiveBayesAnalyzer

df=pd.read_csv('cleaned_anorexia_snippets.csv')
df2=df.sort_values(by='year', ascending=True)

df2['Snippet']=df2['Snippet'].apply(str)

df2['sentiment'] = df2['Snippet'].apply(lambda phrase: TextBlob(phrase).sentiment.polarity)
print (df2['sentiment'])

sns.lineplot(x="year", y="sentiment", data=df2, color='black')
sns.set_theme(style="darkgrid")
plt.xlabel('Year of Publication')
plt.ylabel('Polarity')
plt.title('Sentiment of "anorexia" in $\it{The\ Lancet}$ corpus')
plt.show()
