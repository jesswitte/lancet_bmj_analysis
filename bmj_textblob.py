from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re as re


df = pd.read_json('emaciated_fulltext.jsonl', lines=True)
df2 = df.sort_values(by='datePublished', ascending=True)
df2['fullText'] = df2['fullText'].apply(str)

def pick_only_key_sentence(str1, word):
    result = re.findall(r'([^.]*'+word+'[^.]*)', str1)
    return result

df2['filter_sentence']=df2['fullText'].apply(lambda x : pick_only_key_sentence(x,'emaciated'))
df2['filter_sentence']=df2['filter_sentence'].apply(str)

df2['fullText']=df2['fullText'].apply(str)

df2['sentiment'] = df2['fullText'].apply(lambda phrase: TextBlob(phrase).sentiment.polarity)
print (df2['sentiment'])

#f2['blob'] = [TextBlob(k, analyzer=NaiveBayesAnalyzer()).sentiment.classification for k in df2['filter_sentence']]
df2['sentiment'] = df2['filter_sentence'].apply(lambda phrase: TextBlob(phrase).sentiment.polarity)
print (df2['sentiment'])

sns.lineplot(x="publicationYear", y="sentiment", data=df2, color='black')
sns.set_theme(style="darkgrid")
plt.xlabel('Year of Publication')
plt.ylabel('Polarity')
plt.title('Sentiment of "emaciated" in $\it{The\ British\ Medical\ Journal}$ corpus')
plt.show()

