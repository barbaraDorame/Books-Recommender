"""
Shows percentage of happiness.

feels-opt.py
"""
import pickle
with open('/home/barbara/Documents/NLP/books/library/feelslibrary.p',
          'rb') as hindle:
    data = pickle.load(hindle)


def rescale(values, new_min=0, new_max=100):
    output = []
    old_min, old_max = min(values), max(values)
    for v in values:
        new_v = (new_max - new_min) / (old_max - old_min) * \
                (v - old_min) + new_min
        output.append(new_v)
    return output


negativeness = []
positiveness = []
for book in data:
    negativeness.append(book['Negativeness'])
    positiveness.append(book['Positiveness'])

new_neg = rescale(negativeness)
new_pos = rescale(positiveness)
for book in data:
    book['Negativeness'] = new_neg.pop(0)
    book['Positiveness'] = new_pos.pop(0)
    print(book['Id'], 'Positividad: ', book['Positiveness'])
    print(book['Id'], 'Negatividad: ', book['Negativeness'])

with open('/home/barbara/Documents/NLP/books/library/normlibrary.p',
          'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
