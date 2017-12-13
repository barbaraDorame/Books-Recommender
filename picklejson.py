"""
Shows percentage of happiness.

feels-opt.py
"""
import json

with open('jsonpickle.json', 'rb') as handle:
    data = json.load(handle)

for book in data:
    print(book['Id'], book['Topic'])
