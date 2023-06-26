'''================================== Strings =================================='''
# Immutable data type to store character sets. Enclosed in quotation mkars

# string = 'This is string enclosed in single quotation marks'
# string2 = "This is string enclosed in double quotation marks"
# # string3 = "Wrong'
# string4 = "Don't"
# string5 = 'he: "Hello"'
# string6 = '''
# Hello
# World
# This is still text
# '''
# string7 = """
# Hi
# How are you
# I am the python code
# """

# print(string7)

""" escaped sequences """
# char sequence, starts with -> \
'\n' #-> breacks line
'\t' #-> tab symbol
'\\' #-> to use \ type two \\
'\'' #-> to use single quotation mark in string wich was started with single quotation mark, same fo double quotation mak
'\r' #-> returns caret to beggining
'\v' #-> vertical tab

# string = 'Hello wrold vamos ruthm how do we \n\tSequence \\ don\'t\n\tVamos!\vUWU' 
# print(string)


'''Concatonation'''
# str_1 = "Hello"
# str_2 = 'World'
# print(str_1 + ' ' + str_2)


''' Dublication '''
# print(str_1, str_1, str_1)
# print((str_1+' ')*100)


''' Dynamic string or format '''

# 1. Using % sign
# 2. With using method of .format()
# 3. string interpolation

# name = input("Enter your name: ")

# %
# result = 'Hello, %s' %name
# print(result)

# .format
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# result = 'Hello, {}. Your age: {}'.format(name, age)
# print(result)

# f-string
# res = f'Hi, {name}. Your birth year is {2023 - int(age)}'
# print(res)


''' Indexes '''
# Seuqence Number of string
' h e l l o   w o r l d'
# 0 1 2 3 4 5 6 7 8 9 10
# str_ = 'hello world'
# print(str_[0])
# str_[1] # second char
# str_1[-1] # last char

''' Slices '''
# accessing to some subsequence of string
# synctax [start: end - 1: step]
# print(str_[: 5]) 
# print(str_[6: ])
# print(str_[:-1])
# print(str_[1:-1])
# print(str_[::2])

# print('Hello'[::-1])


''' String methods '''
# print(dir(str))
# is methods. returns boolean type
# str.isalnum() # cheks if string consists from letters and numbers -> bool
# str.isalpha() # cheks if string consists only from letters -> bool
# str.isdecimal() # cheks if string contains only decimal -> bool
# str.isdigit() # cheks if string contains only digit -> bool
# str.islower() # cheks if string in lowercase -> bool
# str.isupper() # cheks if string in uppercase -> bool
# str.isspace() # cheks if string is empty -> bool
# str.isnumeric() # cheks if string contains only numbers -> bool

# str.upper() # converts to uppercase
# str.lower() # converts to lowercase
# str.swapcase() # swaps the cases. lower to upper, upper to lower

# str.replace(old, new, count) -> replaces new instead old substring 
# str.strip() -> trim
# str.lstrip() -> left trim
# str.rstrip() -> right trim
