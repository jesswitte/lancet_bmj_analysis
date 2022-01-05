import glob
from difflib import SequenceMatcher
import pandas as pd
from nltk import tokenize
import os

source = ('/Users/jessicawitte/Documents/hathiscrape_lancet/hathi_vols/**/*.txt')
files2get = glob.glob(source + '9*.txt')
files2get.extend(glob.glob(source + '8*.txt'))


targets = {'anxiety'}

snippets = []
filenames = []
indexes = []

for filename in source:
    with open(filename, encoding = 'utf-8') as f:
filestring = f.read()
wordsinfile = tokenize.word_tokenize(filestring)

for idx, w in enumerate(wordsinfile):
    found = False
if w in targets:
    found = True
w = w.lower()
elif w.startswith('p') and len(w) > 4:

for t in targets:
    matcher = SequenceMatcher(None, w, t)
if matcher.real_quick_ratio() > 0.5 and matcher.ratio() > 0.85:
    found = True
break

if found:
    snippetstart = idx - 25
    if snippetstart < 0:
        snippetstart = 0

    snippetend = idx + 25
    if snippetend > len(wordsinfile):
        snippetend = len(wordsinfile)


    snippets.append((' '.join(wordsinfile[snippetstart : snippetend])))
    if len(snippets) % 10 == 1:
        print(len(snippets))

    indexes.append(idx)




print (snippets)















