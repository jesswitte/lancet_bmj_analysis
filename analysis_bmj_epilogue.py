from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob
import pandas as pd
import re as re

df = pd.read_json('emaciated_fulltext.jsonl', lines=True)
df2 = df.sort_values(by='datePublished', ascending=True)
df2['fullText'] = df2['fullText'].apply(str)

def pick_only_key_sentence(str1, word):
    result = re.findall(r'([^.]*'+word+'[^.]*)', str1)
    return result

df2['filter_sentence']=df2['fullText'].apply(lambda x : pick_only_key_sentence(x,'emaciated'))
df2['filter_sentence']=df2['filter_sentence'].apply(str)


df2['sentiment'] = df2['filter_sentence'].apply(lambda phrase: TextBlob(phrase).sentiment.polarity)

df2 = df2.sort_values(by='sentiment', ascending=False)
df2 = df2.drop_duplicates(['filter_sentence'])
pos_df = df2[0:31]
pos_df.to_csv('pos_bmjemaciatedblob.csv')

df2 = df2.sort_values(by='sentiment', ascending=True)
df2 = df2.drop_duplicates(['filter_sentence'])
neg_df = df2[0:31]
neg_df.to_csv('neg_bmjemaciatedblob.csv')

