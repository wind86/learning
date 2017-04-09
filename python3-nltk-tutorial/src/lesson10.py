'''
Created on Apr 09, 2017

Wordnet with NLTK
https://www.youtube.com/watch?v=T68P5-8tM-Y&index=10&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

@author: ubuntu
'''
from nltk.corpus import wordnet

syns = wordnet.synsets("program")

print(syns[0].name())

print(syns[0].lemmas()[0].name())

print(syns[0].definition())

print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w3 = wordnet.synset('ship.n.01')
w4 = wordnet.synset('car.n.01')
print(w3.wup_similarity(w4))

w5 = wordnet.synset('ship.n.01')
w6 = wordnet.synset('cat.n.01')
print(w5.wup_similarity(w6))