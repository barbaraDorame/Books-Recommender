"""
que.py.

literalmente que quieres
"""
from gensim import corpora
import gensim
import pickle

with open('/home/barbara/Documents/NLP/books/library/bookstokenized.p',
          'rb') as hindle:
    data = pickle.load(hindle)

lista = [book['Text'] for book in data]
dictionary = corpora.Dictionary(lista)
bow = [dictionary.doc2bow(book) for book in lista]
ldamodel = gensim.models.ldamodel.LdaModel(bow, num_topics=20,
                                           id2word=dictionary, passes=20,
                                           minimum_probability=0)

print(ldamodel.print_topics(num_topics=18, num_words=10))
# 3:32
with open('/home/barbara/Documents/NLP/books/library/topics1.p',
          'wb') as handle:
    pickle.dump(ldamodel, handle, protocol=pickle.HIGHEST_PROTOCOL)
