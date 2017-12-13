import sys
import os
import shutil
import zipfile
from bs4 import BeautifulSoup
import pickle

i = 0
for path, subdirs, files in os.walk('/home/barbara/gutenberg'):
    for name in files:
        if name.endswith('.zip'):
            try:
                shutil.move(path+'/'+name, '/home/barbara/gutenberg')
            except:
                pass
            i += 1

for path, subdirs, files in os.walk('/home/barbara/gutenberg'):
    for name in files:
        try:
            exampleZip = zipfile.ZipFile(os.path.join(path, name))
            print('Zipfile: ', name)
            exampleZip.extractall('/home/barbara/gutenberg')
            exampleZip.close()
        except:
            print('No quise zipear el ', name)
            pass


i = 0
for path, subdirs, files in os.walk('/home/barbara/gutenberg/feils/'):
    for name in files:
        if name.endswith(".html") or name.endswith(".htm"):
            try:
                shutil.move(path+'/'+name, '/home/barbara/gutenberg')
                print(i, 'Estoy moviendo ', name, ' por que quiero')
            except:
                print(i, 'No estoy moviendo ', name, ' por que no quiero')
                pass
            i += 1

i = 1
lista = []
for path, sundirs, files in os.walk('/home/barbara/Documents/NLP/' +
                                    'books/gutenberg/'):
    for name in files:
        lein = name.replace('-h.htm', '')
        lein = lein.replace('l', '')
        with open('/home/barbara/Documents/NLP/books/rdf-files/cache/epub/' +
                  lein + '/pg' + lein + '.rdf', 'rb') as books:
            soup = BeautifulSoup(books, 'xml')
            dic = {'Id': str(i)}
            tag = soup.find('rdf:RDF').find('pgterms:ebook') \
                .find('dcterms:title')
            dic['Title'] = tag.text
            try:
                tag = soup.find('rdf:RDF').find('pgterms:ebook') \
                    .find('dcterms:creator').find('pgterms:agent') \
                    .find('pgterms:name')
                dic['Author'] = tag.text
            except:
                dic['Author'] = 'Unkown'
        with open('/home/barbara/Documents/NLP/books/gutenberg/' +
                  name, 'rb') as books:
            soup = BeautifulSoup(books, 'lxml')
            for tag2 in soup.find_all('pre'):
                tag2.replaceWith('')
            text1 = soup.body.get_text()
            dic['Text'] = text1
        lista.append(dic)
        print(i, dic['Title'], '    DONE')
        i += 1

with open('/home/barbara/Documents/NLP/books/library/bookslibrary.p',
          'wb') as handle:
    pickle.dump(lista, handle, protocol=pickle.HIGHEST_PROTOCOL)
