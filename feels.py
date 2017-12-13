"""
Determina la frecuencia de positividad y negatividad de un libro.

el pickle bookslibrary.p

feels.py
"""
import pickle
import math
from nltk import word_tokenize


def tf(word, blob):
    return blob.count(word) / len(blob)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


with open('/home/barbara/Documents/NLP/books/library/bookstokenized.p',
          'rb') as hindle:
    data = pickle.load(hindle)

with open('negative-words.txt', 'r') as f:
    negativewords = f.read()
negativewords = word_tokenize(negativewords)
with open('positive-words.txt', 'r') as fu:
    positivewords = fu.read()
positivewords = word_tokenize(positivewords)

for book in data:
    testpositive = [book['Text'], positivewords]
    testnegative = [book['Text'], negativewords]
    for i, test in enumerate(testpositive):
        scorespositive = {word: tfidf(word, test,
                          testpositive) for word in test}
        wordspositive = sorted(scorespositive.items(),
                               key=lambda x: x[1], reverse=True)
        totalscore = 0
        for word, score in wordspositive[:]:
            totalscore += score
        print(book['Id'], 'Positive percentage: ', totalscore)
        book['Positive'] = totalscore

    for i, test in enumerate(testnegative):
        scoresnegative = {word: tfidf(word, test,
                          testnegative) for word in test}
        wordsnegative = sorted(scoresnegative.items(),
                               key=lambda x: x[1], reverse=True)
        totalscore = 0
        for word, score in wordsnegative[:]:
            totalscore += score
        print(book['Id'], 'Negative percentage: ', totalscore)
        book['Negative'] = totalscore

with open('/home/barbara/Documents/NLP/books/library/feelslibrary.p',
          'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
