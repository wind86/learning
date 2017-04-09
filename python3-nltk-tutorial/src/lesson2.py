'''
Created on Apr 09, 2017

Stop words with NLTK
https://www.youtube.com/watch?v=w36-U-ccajM&index=2&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

@author: ubuntu
'''
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)