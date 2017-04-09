'''
Created on Apr 09, 2017

Text Classification with NLTK
https://www.youtube.com/watch?v=zi16nl82AMA&index=11&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

@author: ubuntu
'''
import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print(documents[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])