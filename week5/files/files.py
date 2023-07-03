"""Working with files. Modules and packages. JSON"""

"""========= Working with files ========="""

# open('path/to/file')

# file1 = open('./text.txt')
# print(file1)
# file2 = open('text.txt', 'w')
# file2.write('Hello World!')
# print(file2)


'=========== Modes ============'

# 1. r (read) -> opens file for reading
# if file does not exist then raises Error
# file1 = open('text.py')
# file2 = open('text.py', 'r')

# 2. w (write) -> opens file for writing
# overrides all file e. g cleans all file and writes
# if file does not exist then it creates file with path/name
# file1 = open('test.py', 'w')

# 3. a (append) -> opens file for appending
# All new lines add to the end of file
# If file does not exist then it creates file with 'path/name'
# file1 = open('hello.py', 'a')

# 4. x(exclusive) -> creates file with unique name. If file in directory exist the it raises Error

# 5. t (text) -> opens file wint text mode

# 6. b (binary) -> opens file in binary mode


# file2 = open('text.txt', 'r+')
# print(file2.read())
# file2.write('\nMakers')

"""Methods"""

# read() reads all file
# readline() reads only one line
# readlines() reads all lines and return list of lines

# with open('text.txt') as file:
#   print(file.read(10))
#   print(file.readline())
#   print(file.readline())
#   print(file.readline())
#   print(file.readline())
#   print(file.readline())
#   print(file.readlines())

"""Methods in w mode"""
# write('string') -> writes string into file
# writelines(list[str])

# f = open('text.txt', 'w')
# f.write('Hello World!')
# f.write('\nHello Makeres!')
# f.writelines(['\nHello Adil!', '\nHello Kyrgyzstan!1'])

# """Methods in """
# with open('test.py', 'w') as file:
#     file.writelines(["print(\'Hello World!\')\n" for _ in range(2000)])

"""JSON"""
"""
JSON (JavaScript Object Notation)
"""

import json
# print(dir(json))
"""Serialization and Deserialization"""
# Serialization -> write data in JSON
# dump() -> reads python object and converts to JSON and writes to .json file
# dumps() -> does same thing as dump, but it returns json string

# Deserialization
# load() -> method which reads JSON file and converts to Python object
# loads() -> method which reads JSON string and converts to Python object

# with open('data.json', 'r+') as file:
#     data = json.load(file)
#     data.append({
#         "John": {
#             "age": 19,
#             "gender": "F",
#             "stack": ["React.js", "TypeScript", "HTML", "CSS"]
#         }
#     })
#     file.seek(0)
#     file.write(json.dumps(data))

import json
from typing import List, Dict


def get_product(id: int, prod_list: List) -> Dict:
    prod = None
    for product in prod_list:
        if product['id'] == id:
            prod = product
            break
    if not prod:
        raise ValueError()
    return prod


def update(id: int, title: str = None, price: int = None, rating: float = None) -> None:
    update_product = {
        'title': title,
        'price': price,
        'rating': rating
    }

    with open('new_db.json') as file:
        new_db = json.load(file)

    product = get_product(id, new_db)
    new_db.remove(product)

    for k, v in update_product.items():
        if v:
            product[k] = v

    new_db.append(product)

    with open('new_db.json', 'w') as file:
        file.write(json.dumps(new_db))


