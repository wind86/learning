'''
Created on Apr 09, 2017

Lemmatizing with NLTK
https://www.youtube.com/watch?v=uoHVztKY6S4&index=8&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

@author: ubuntu
'''
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))