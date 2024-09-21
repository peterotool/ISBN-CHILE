# https://gist.github.com/catawbasam/c52dbc22edb9e9c624b2cac9099f812c

import json

import pandas as pd

#load
path = 'books/book_test.json'
with open(path, encoding='utf-8') as f:
    lines = f.readlines()


json_array = []
for l in lines:
    json_array.append( json.loads(l))

df = pd.DataFrame(json_array)
print(df)