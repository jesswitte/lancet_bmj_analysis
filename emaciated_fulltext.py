import pandas as pd
import re as re
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc

df = pd.read_json('emaciated_fulltext.jsonl', lines=True)
df2 = df.sort_values(by='datePublished', ascending=True)
df2['fullText'] = df2['fullText'].apply(str)

print(df2['datePublished'])

def pick_only_key_sentence(str1, word):
    result = re.findall(r'([^.]*'+word+'[^.]*)', str1)
    return result
df2['filter_sentence']=df2['fullText'].apply(lambda x : pick_only_key_sentence(x,'emaciated'))

analyzer = SentimentIntensityAnalyzer()
df2['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df2['filter_sentence']]
df2['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df2['filter_sentence']]
df2['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df2['filter_sentence']]
df2['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df2['filter_sentence']]

sns.lineplot(x="publicationYear", y="compound", data=df2, color='black')
sns.set_theme(style="darkgrid")
plt.xlabel('Year of Publication')
plt.ylabel('Polarity')
plt.title('Sentiment of "emaciated" in $\it{The\ British\ Medical\ Journal}$ corpus')
plt.show()


