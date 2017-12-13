"""
que.py.

literalmente que quieres
"""
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle

with open('/home/barbara/Documents/NLP/books/library/bookslibrary.p',
          'rb') as hindle:
    data = pickle.load(hindle)

for book in data:
    book['Text'] = book['Text'].lower()
    puncList = [".", ";", ":", "!", "-", "\'", "?", "/", "\\", ",", ")",
                "(", "\"", '\'s', '--', '\'ll', '\'t', 'n\'t', '\\\'t',
                "”", "“", "’", "{", "}", "[", "]", "&", "1", "‘"]
    for punc in puncList:
        book['Text'] = book['Text'].replace(punc, '')

    book['Text'] = word_tokenize(book['Text'])

    stopwordslist = set(stopwords.words("english"))
    for stop in stopwordslist:
        book['Text'] = [word for word in book['Text'] if word != stop]
    stopwordslist = set(stopwords.words("spanish"))
    for stop in stopwordslist:
        book['Text'] = [word for word in book['Text'] if word != stop]

    p_stemmer = PorterStemmer()
    book['Text'] = [p_stemmer.stem(word) for word in book['Text']]

    print('Terminé con', book['Id'])

with open('/home/barbara/Documents/NLP/books/library/bookstokenized.p',
          'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
