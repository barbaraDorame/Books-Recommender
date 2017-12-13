"""
Shows percentage of happiness.

feels-opt.py
"""
import logging
from gensim import corpora, models, similarities
import pickle

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

with open('/home/barbara/Documents/NLP/books/library/bookstokenized.p',
          'rb') as hindle:
    data = pickle.load(hindle)

with open('negative-words.txt', 'r') as f:
    negativewords = f.read()
negativewords = negativewords

with open('positive-words.txt', 'r') as fu:
    positivewords = fu.read()
positivewords = positivewords

lista = [book['Text'] for book in data]
dictionary = corpora.Dictionary(lista)
corpus = [dictionary.doc2bow(text) for text in lista]
vec_positive = dictionary.doc2bow(positivewords.lower().split())
vec_negative = dictionary.doc2bow(negativewords.lower().split())
tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=270433)
positive = index[tfidf[vec_positive]]
negative = index[tfidf[vec_negative]]
listap = []
listan = []
for i, per in list(enumerate(positive)):
    listap.append(per)
for i, per in list(enumerate(negative)):
    listan.append(per)
for book in data:
    book['Negativeness'] = listan.pop(0)
    book['Positiveness'] = listap.pop(0)
    print(book['Id'], 'Positividad: ', book['Positiveness'])
    print(book['Id'], 'Positividad: ', book['Negativeness'])

with open('/home/barbara/Documents/NLP/books/library/feelslibrary.p',
          'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
# print('Porcentaje positivo: ', list(enumerate(positive)))
# print('Porcentaje negativo: ', list(enumerate(negative)))
