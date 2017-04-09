'''
Created on Apr 09, 2017

Tokenizing Words and Sentences with NLTK
based on https://www.youtube.com/watch?v=FLZvOKSCkxY&index=1&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

@author: ubuntu
'''
import nltk

# nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))

for word in word_tokenize(EXAMPLE_TEXT):
    print(word)