'''
Created on Apr 09, 2017

The corpora with NLTK
https://www.youtube.com/watch?v=TKAXDqoG2dc&index=9&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

@author: ubuntu
'''
import nltk
# print(nltk.__file__)

from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])