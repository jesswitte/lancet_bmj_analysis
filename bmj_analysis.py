from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pd.options.display.max_colwidth = 30000
df = pd.read_json('emaciated_fulltext.jsonl', lines=True)
df2 = df.sort_values(by='datePublished', ascending=True)
df2['fullText'] = df2['fullText'].apply(str)
print(df2['fullText'], df2['datePublished'])
#print (df.head(5))

print(df.columns)

analyzer = SentimentIntensityAnalyzer()
df2['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df2['fullText']]
df2['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df2['fullText']]
df2['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df2['fullText']]
df2['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df2['fullText']]


print(df2)

sns.lineplot(x="datePublished", y="neg", data=df2)
sns.set_theme(style="darkgrid")
plt.xlabel('Year of Publication')
plt.ylabel('Negative Polarity')
chart.xaxis.set_major_locator(mdates.YearLocator(base=1))
chart.margins(x=0)
chart.set_xticks(chart.get_xticks()[::10])
plt.show()

df2['fullText'] = df2['fullText'].astype(str)

df2['sentiment'] = df2['fullText'].apply(lambda tweet: TextBlob(tweet).sentiment)
print(df2)



