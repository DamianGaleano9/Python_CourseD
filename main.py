from decimal import Decimal
import numpy as np
# Python String Basics

# """"
# starter_sentence = "The quick brown fox jumped"
# first_word = starter_sentence[0]
# print(first_word)
# sentence = "HELLO THERE!"
# lowercase_sentence = sentence.lower()
# print(lowercase_sentence)
# """


# #In the code below, assign the variable sub_sentence to be "pie" by selecting a range from "sentence".

# """sentence = "Some pie please!"
# sub_sentence = sentence[5:8]
# print(sub_sentence)
# """

# """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.
# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.
# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """

# my_heredoc = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.
# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.
# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# .strip()

# """
# print(my_heredoc)


# """
# [
#     [0, 1, 2, 3, 4],
#     [1, 2, 3, 4, 5],
#     [2, 3, 4, 5, 6],
#     [3, 4, 5, 6, 7],
#     [4, 5, 6, 7, 8],
# ]
# """


# def manual_incrementing_matrix(n):
#   matrix = [[None for y in range(n)] for x in range(n)]

#   counter = 0

#   for idx, el in enumerate(matrix):
#     for nested_idx, nested_el in enumerate(el):
#       matrix[idx][nested_idx] = counter + nested_idx

#       counter += 1

#   return matrix
# print(manual_incrementing_matrix(9))


# users = ["Damian", "Salvador", "Massimo"]
# print(users)

# users.append("Ana")
# print(users)

# tags = ["python", "development", "tutorial", "code"]


# number_of_tags = len(tags)
# last_item = tags[-1]
# index_of_last_item = tags.index(last_item)
# print(number_of_tags)
# print(last_item)
# print(index_of_last_item)


# product_id = 123 #enter
# float_number = 12.99 #float
# fraction_number = 1/5
# new_float_number  = float(product_id)
# new_product_number = product_id + fraction_number

# print(new_float_number)
# print(type(product_id))
# print(type(float_number))
# print(type(fraction_number))
# print(new_product_number)


# print('Addition')
# print(100 + 200)
# print('---')

# print('Subtraction')
# print(200 -199)
# print('---')

# print('Division')
# print(12.99/ 12.8888888)
# print('---')

# print('Floor Division') # Return an integer
# print(12.99 // 12.8888888)
# print('---')

# print('Multiplication')
# print(4.3 * 12.4)
# print('---')

# print('Modulus')
# print(1 & 13)
# print('---')

# print('Exponential')
# print(2 ** 2)

# Please ---- Parentheses ()
# Excuse  ------ Exponents ***
# My ------ Multiplication *
# Dear ---- Division /
# Aaunt --- Addition +
# Sally --- Subtraction -


# calculation = 9 + 20 * 12 + (20 + 9) ** 2

# print(calculation)


# How to Use Assignment Operators in Python

# total = 100

# total = total + 10

# total += 10
# total-= 10
# total*= 10
# total/= 10
# total//= 10
# total **= 2
# total %= 10


# shoes_new = 250
# tshirt_new = 100

# total += shoes_new
# total += tshirt_new
# discount =  total * 0.2

# new_pack_collection = total - discount

# print(new_pack_collection)


# Decimal vs Float in Python
# from decimal import Decimal calling from top

# product_cost = 88.40
# commision_rate = 0.08 # 8%
# qty = 450 Prin Solution # 42962.4


# product_cost = Decimal(88.40)  #With decimal import
# commision_rate = Decimal(0.08)

# product_cost += (commision_rate * product_cost)
# print(product_cost * qty)  #42962.40000000000282883716451


# product_cost = 29.30
# comission_rate = 0.02

# qty = 960

# print(int(product_cost)) #29 converting integer
# print(float(qty)) #960.0
# print(Decimal(product_cost)) #29.300000000000000710542735760100185871124267578125
# print(complex(comission_rate)) #(0.02+0j)


# Overview of Popular Math Functions in Python

# import math

# loss = -20.25
# product_cost = 89.99


# print(abs(loss))
# print(math.floor(product_cost))
# print(math.ceil(product_cost))
# print(abs(math.floor(loss)))
# print(round(product_cost))
# print(math.sqrt(product_cost))
# print(math.pow(3, 2))
# print((3 ** 2))


"""
Users Database Query

Damian
Massimo
Salvador

"""

# users = ['Damian', 'Massimo', 'Salvador']
# print(users)

# users.insert(0, 'Ana')

# print(users)

# users.append('Isis')
# print(users)

# users[4] = 'Silvestre'

# print(users)

# print(users[1]) #Call like a string
# print([users[1]]) #Call like a list


# users = ['Damian', 'Massimo', 'Salvador']


# users.remove('Damian')
# print(users)


# popped_user = users.pop()

# print(users)
# print(popped_user)
# print(users)
# users.append('Machi')
# print(users)


# del users[1]
# print(users)


# Guide to Nested Lists and Best Practices for Storing Multiple Data Types in a Python List


# users = ['Damian', 'Massimo', 'Salvador', 'Walter', 'Jessy']

# ids = [1, 2, 4]
# countries = ["Colombia", "Spain", "Germany"]
# users.append(countries)
# mixed_list = [ids, users]
# print(mixed_list)

# final_list = mixed_list.pop()


# print(final_list)


# Overview of Python List Query Processes: len(), Negative Indexes, and index()

# tags = ['python', 'javascript', 'react', 'development']

# number_of_tags = len(tags)

# print(number_of_tags)


# last_tag = tags[-1]
# print(last_tag)

# index_of_last_item = tags.index(last_tag)
# print(index_of_last_item)


# How to Sort Lists in Python****

# tags = ['python', 'javascript', 'react', 'development']
# print(tags)

# tags.sort()
# print(tags)
# # ['development', 'javascript', 'python', 'react']


# tags.sort(reverse=True)
# print(tags)
# # ['react', 'python', 'javascript', 'development']


# numbers = [2, 3, 9, 22, 35, 1, 6, 8]
# numbers.sort()
# print(numbers)
# # [1, 2, 3, 6, 8, 9, 22, 35]
# numbers.sort(reverse=True)
# print(numbers)
# [35, 22, 9, 8, 6, 3, 2, 1]


# Using the join Function in Python to Build a URL Query String ***

# https://www.google.com/search?q=python+development+tutorial


# uri = 'https://www.google.com/search?q='
# tags = ['python', 'development', 'tutorial']

# formatted_tags = '+'.join(tags)
# print(formatted_tags)
# # python+development+tutorial

# #Use Interpolation

# query_tags = f'{uri}{formatted_tags}'
# print(query_tags)
# # https://www.google.com/search?q=python+development+tutorial #We have the Same Url from the top


# Overview of Ranges in Python Lists ****

# tags = ['python', 'javascript', 'react', 'development']


# tags_range = tags[1:]
# print(tags_range)
# ['javascript', 'react', 'development']
# tags_range = tags[:-1]
# tags_range = tags[:-1]
# print(tags_range)

# ['python', 'javascript', 'react']


# Advanced Techniques for Implementing Ranges and Slices in Python Lists*****


# tags = [
#   'python',
#   'development',
#   'tutorials',
#   'code',
#   'programming',
#   'computer science'
# ]


# tags_slice_range = tags[1:-1]
# print(tags_slice_range)
# ['development', 'tutorials', 'code', 'programming']#


# tags_slice_range = tags[:-1:2]
# # ['python', 'tutorials', 'programming']#
# print(tags_slice_range)


# tags_slice_range = tags[:-1:4]
# print(tags_slice_range)
# # ['python', 'programming']#


# tags_slice_range = tags[::-1]
# print(tags_slice_range)
# ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']#
# We got inversal list


# tags.sort(reverse=True)
# print(tags)
# ['tutorials', 'python', 'programming', 'development', 'computer science', 'code']#


# forbidden_tags = tags.sort(reverse=True)
# print(forbidden_tags)
# None# Inmutability python is not allowed


# sales_prices = [
#     100,
#     300,
#     129,
#     23,
#     36,
#     99
# ]

# sales_prices.sort()
# print(sales_prices)
# [23, 36, 99, 100, 129, 300]#

# sorted_sales_prices = sales_prices.sort()
# print(sorted_sales_prices)
# None#

# sorted_sales_prices = sorted(sales_prices)
# print(sorted_sales_prices)
# [23, 36, 99, 100, 129, 300]
# We can store the variable with sorted with sort not

# sorted_list = sorted(sales_prices, reverse=True)
# print(sorted_list)
# [300, 129, 100, 99, 36, 23]#


# import numpy as np from the top#

# data = [19, 18, 17, 9, 6, 3, 2, 1, 8, 26, 35]

# print("Media: ", np.mean(data))
# print("Mediana: ", np.median(data))
# print("Desviacion Estandar: ", np.std(data))
# print("Variancia: ", np.var(data))

# # Media:  13.090909090909092
# # Mediana:  9.0
# # Desviacion Estandar:  10.378776819281875
# # Variancia:  107.7190082644628

# first_name = "Damian"
# last_name = "Mazo"


# def function(first_name, last_name):
#     greeting = f"Hello, {first_name} {last_name}"


#     return greeting


# print(function(first_name, last_name))


# How to Find the Median of a Python List with an Odd Number of Numbers#

"""
Tools :
-math library
-sorted function
-list slicing function
-computation

# """
# import math

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# # sale_prices.sort
# # print(sale_prices)
# # [100, 83, 220, 40, 100, 400, 10, 1, 3]#

# sorted_list = sorted(sale_prices)
# # print(sorted_list)
# # [1, 3, 10, 40, 83, 100, 100, 220, 400]#

# num_of_sales = len(sorted_list)
# # print(num_of_sales)
# # 9#

# # first_sales_item = sorted_list[:math.floor(num_of_sales/2)]
# # print(first_sales_item)
# # [1, 3, 10, 40]  #We take the first 4 element with math, we know the num


# last_item_sales = sorted_list[-(math.floor(num_of_sales/2)):]
# print(last_item_sales)
# # [100, 100, 220, 400]#

# half_slices = math.floor(num_of_sales/2) #We create this variable best practices
# median = sorted_list[half_slices:(half_slices) + 1]
# print(median)
# # [83]#


# tags = [
#     'pythons',
#     'javascript',
#     'development',
#     'data',
#     'tutorials'
# ]

# # print(tags[:2])
# # ['pythons', 'javascript']#

# slice_object = slice(2)

# # print(slice_object)
# # slice(None, 2, None)#


# print(tags[slice_object])
# ['pythons', 'javascript'] #We have the same behavior


# slice_object = slice(1, 2, 9)

# print(slice_object.start)
# # 1#
# print(slice_object.stop)
# # 2#
# print(slice_object.step)
# # 9#


# How to Add to a List in Python with Both In Place and Copy Processes

# tags = ['pythons', 'javascript', 'tutorials']

# Nope

# tags[-1] = 'programming'
# print(tags) # This way remove the original list

# tags.extend('react')
# print(tags) # This way add the element separted


# tags.extend(['react'])
# print(tags)
# ['pythons', 'javascript', 'tutorials', 'react']#

# Correct way to add


# new_tag = tags + ['react']
# tags.extend(['Damian'])

# print(new_tag)
# # ['pythons', 'javascript', 'tutorials', 'react']#

# print(tags)
# # ['pythons', 'javascript', 'tutorials']#

# players = {
#     "ss": "Correa",
#     "2b": "Altuve",
#     "3b": "Bregman",
#     "DH": "Gattis",
#     "OF": "Springer",
# }

# # print(players)

# second_player = players["2b"]
# last_player = players["OF"]
# dessignated_player = players["DH"]


# print(second_player)
# print(dessignated_player)
# print(last_player)
# # Altuve
# # Gattis
# # Springer

# How to Add New Key/Value Pairs to Python Dictionaries

# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujols"],
#     "yankees": ["Judge", "Stanton"]
# }

# teams["Barcelona"] = ["Messi", "Ronaldinho"]


# # featured_teams = teams["Madrid"]
# # print(teams)
# # KeyError: 'Madrid'#

# featured_teams_new = teams.get("Barcelona", "Not Found it")

# # print(featured_teams_new)

# print(id(teams))
# 2108982734208


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list[0] = 99

# print(id(list))
# 1954884664384


# list[0] = 1
# print(id(list))


# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True',
# 'and', 'as', 'assert', 'async',
#  'await', 'break', 'class', 'continue'
#  , 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
# 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']


# players = {
#     "ss": "Correa",
#     "2b": "Altuve",
#     "3b": "Bregman",
#     "DH": "Gattis",
#     "OF": "Springer",
# }
# # print(players.keys())
# # dict_keys(['ss', '2b', '3b', 'DH', 'OF'])#

# # print(players.values())
# # dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])#

# # print(players.items())
# # # dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])#
# # #Returns a tuple

# # print(players.keys()[0])
# # TypeError: 'dict_keys' object is not subscriptable
# #We can't use  dict_keys isn't not a list

# #For to fix this

# # players_names = list(players.copy().values())

# # print(players_names)
# # ['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer']


# # Correa#
# # ['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer']#
# # We have a list of players converting to lists


# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujols"],
#     "yankees": ["Judge", "Stanton"],
#     "red sox" : ["Messi", "Ronaldinho"]
# }


# team_groupings = teams.items()
# # print(team_groupings)
# # dict_items([('astros', ['Altuve', 'Correa', 'Bregman']), ('angels', ['Trout', 'Pujols']),
# # ('yankees', ['Judge', 'Stanton']), ('red sox', ['Messi', 'Ronaldinho'])])
# print(list(team_groupings)[3][1][0])
# ('astros', ['Altuve', 'Correa', 'Bregman']) # We convert the have a tuple
# # Messi#

# Overview of the Multiple Methods for Deleting Items in a Python Dictionary#


# teams = {
#     "astros": ["Altuve", "Correa", "Bregman"],
#     "angels": ["Trout", "Pujols"],
#     "yankees": ["Judge", "Stanton"],
#     "red sox" : ["Messi", "Ronaldinho"]
# }


# del teams["angels"]
# print(teams)


# {'astros': ['Altuve', 'Correa', 'Bregman'],
#  'yankees': ['Judge', 'Stanton'], 'red sox': ['Messi', 'Ronaldinho']}#


# del teams["Madrid"]
# print(teams.get("Madrid", "No team found"))

# remove_teams = teams.pop("red sox","No team found")
# print(remove_teams)


# teams = [
#     {
#         'astros': {
#             '2B': 'Altuve',
#             'SS': 'Correa',
#             '3B': 'Bregman',
#         }
#     },
#     {
#         'angels': {
#             'OF': 'Trout',
#             'Dh': 'Pujols',
#         }
#     }
# ]


# print(teams[0])
# {'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}#

# angels = teams[1].get("angels", "No team found")
# print(list(angels.values())[1])
# # dict_values(['Trout', 'Pujols'])#
# # Pujols#

# angels_new = teams[1].get('angels', 'Team not found')
# print(list(angels_new.values())[0])
# # Trout#


# Build a Histogram in Python with No 3rd Party Libraries#

# sales = {
#   'google': 20,
#   'facebook': 42,
#   'twitter': 2,
#   'offline': 12,
# }


# print('g ' + sales['google'] * '$')
# print('f ' + sales['facebook'] * '$')
# print('t ' + sales['twitter'] * '$')
# print('o ' + sales['offline'] * '$')

# g $$$$$$$$$$$$$$$$$$$$
# f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# t $$$$$$$$$$
# o $$$$$$$$$$$$


# LIST
# DICTIONARY
# TUPLE


# Tuple = Inmmutable
# list  = mutable

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content' )


# #Tuple unpacking
# title, sub_heading, content = post

# This create a query engine

# title = post[0]
# sub_heading = post[1]
# content = post[2]

# print(title)
# print(sub_heading)
# print(content)


# post = ('Python Basics', 'Intro guide to python', 'Some cool python content' )
# print(id(post))
# 2876106480320


# post = post + ('published',)
# post += ('35')
# print(id(post))
# 2312233874224
# #Unpacking

# title, sub_heading, content, status, age= post

# print(title)
# print(sub_heading)
# print(content)
# print(status)
# Intro guide to python
# Some cool python content
# published

# # Working with Lists Nested in Tuples#
# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')
# tags = ['python', 'tuple', 'list']


# post += (tags,)

# # print(post)
# ('Python Basics', 'Intro guide to python', 'Some cool python content', 'tags')
# print(post)
# ('Python Basics', 'Intro guide to python', 'Some cool python content', ['python', 'tuple', 'list'])
# print(post[-1][1])
# ['python', 'tuple', 'list']

# Three Ways to Remove Elements from a Python Tuple#

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')
# post = list(post)
# # print(post)
# post.remove('Python Basics')
# # print(post)
# post = tuple(post)
# print(post)
# post += ('Python Basics',)
# print(post)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# primera_posicion =  numeros[0]
# print(primera_posicion)


# longitud_lista = len(numeros)
# print(f"El primer elemento de la lista es: {primera_posicion}\nla longitud de la lista es: {longitud_lista}" )


# for num in numeros:
#     print(num)

# new_list = ["You", "Are", "Amazing", "Great", "person"]

# ultima_posicion = new_list[-1]
# print(ultima_posicion)

# penultima_posicion = new_list[-2]
# print(penultima_posicion)

# elementos_del_centro = new_list[1:-1]
# print(elementos_del_centro)

# center_element = new_list[2]
# print(center_element)


# list_name = ["Damian", "Ana", "Massimo", "Salvador"]

# name = "Ana"
# other_name = "Isis"


# if name in list_name:
#     print(f"The name is here and is {name}")

# if other_name not in list_name:
#         print(f"Name is {other_name}")


# modify elements of a list

# lenguajes = ["pythons", "react", "javascript"]

# # new_lenguage = lenguajes[0]
# lenguajes[0] = "Ruby"


# print(lenguajes)
# # ['Ruby', 'react', 'javascript']#
# lenguajes[0:2] = ["html", "css"]

# print(lenguajes)
# # ['html', 'css', 'javascript']#
# lenguajes.insert(0, "Damian")
# print(lenguajes)
# # ['Damian', 'html', 'css', 'javascript']#

# lenguajes.append("Sass")
# print(lenguajes)


# lists_name = ["Damian", "Ana", "Salvatore"]


# lenguajes.extend(lists_name)
# print(lenguajes)
# ['Damian', 'html', 'css', 'javascript', 'Sass', 'Damian', 'Ana', 'Salvatore']


# lists_name = ["Damian", "Ana", "Salvatore"]

# # for x in lists_name:
# #         print(x)

# lists_name[1] = "Maria"
# print(lists_name)

# lists_name.insert(1, "Ana")
# print(lists_name)
# lists_name.pop()
# print(lists_name)


# post = ('Python Basic', 'Intro guide to Python', 'Published')
# post = list(post)
# print(post)
# post[0] = "JavaScript"
# print(post)
# post = tuple(post)
# print(post)


# list_number = [1, 12, 31, 4, 5, 36, 78, 8]
# list_number.sort()
# print(list_number)

# list_number.sort(reverse=True)
# print(list_number)

# # How to Use a Tuple as a Dictionary Key in Python#
# priority_index = {
#     (1, 'premier'): [1, 34, 9],
#     (1, 'mvp'): [1, 34, 9],
#     (2, 'standard'): [99, 81, 2]
# }

# # print(list(priority_index.keys()))
# # # [(1, 'premier'), (1, 'mvp'), (2, 'standard')]#
# # print(list(priority_index.values()))
# # # [[1, 34, 9], [1, 34, 9], [99, 81, 2]]#
# # print(list(priority_index.items()))

# print(list(priority_index.keys())[0][1])
# priority_index ['age'] = 'Damian'
# print(list(priority_index))

# Guide to Python's Zip Function#

# positions = ['1p', '2p', '3p']
# players = ['Damian', 'Ana', 'Salvador']

# mixing_list = zip(positions, players)
# # <zip object at 0x000001C4EC542680>#
# #We have a zip objet we need to call list Function for to merge
# print(list(mixing_list))
# # [('1p', 'Damian'), ('2p', 'Ana'), ('3p', 'Salvador')]#

# Uniqueness

# tags = {
#     'python',
#     'javascript',
#     'react'
# }

# print((tags))

# query_one = 'python' in tags
# print(query_one)


# Various Methods for Merging Python Sets#


# tags_one = {
#     'python',
#   'coding',
#   'tutorials',
#   'coding'
# }

# tags_two = {
#     'ruby',
#   'coding',
#   'tutorials',
#   'development'
# }


# merged_tags = tags_one | tags_two
# print(merged_tags)
# # {'python', 'tutorials', 'ruby', 'development', 'coding'}#
# exclusive_to_tag_one = tags_one - tags_two
# print(exclusive_to_tag_one)
# # {'python'}#
# exclusive_to_tag_two = tags_two - tags_one
# print(exclusive_to_tag_two)
# # {'ruby', 'development'}#

# universals_tags = tags_one & tags_two
# print(universals_tags)

"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Hi there','3')
<h3>Hi There </h3>

"""

# def heading_generator(title, heading_type):
#   return f'<h{heading_type}>{title}</h{heading_type}>'


# print(heading_generator('Hy Damian', '1'))
# print(heading_generator('Hy Ana', '2'))
# print(heading_generator('Hy Salvado', '3'))
# print(heading_generator('Hy Massimo', '4'))
# <h1>Hy Damian</h1>
# <h2>Hy Ana</h2>
# <h3>Hy Salvado</h3>
# <h4>Hy Massimo</h4>

# How to Implement Python Loops for Lists, Tuples, and Dictionaries#


# players = ["Damian", "Salvador", "Massimo", "Ana"]

# for var in players:
#     print(var)

# It works the same way


# players = ("Damian", "Salvador", "Massimo", "Ana")

# for var in players:
#     print(var)

# names = {
#     '10': 'messi',
#     '7': 'Cristiano',
#     '3': 'Roberto Carlos',
# }


# for numbers, players in names.items():
#   print('Name T-shirt', numbers)
#   print('Name ', players)
# # Name T-shirt 10
# # Name  messi
# # Name T-shirt 7
# # Name  Cristiano
# # Name T-shirt 3
# # Name  Roberto Carlos

# def loop_over_list():
#     # Write your code here
#       my_list = ["Damian", "Salvador", "Massimo", "Ana", "Isis"]
#       for x in my_list:
#         print(x)

#         return my_list

# alphabet = 'abcdef'

# for letter in alphabet:
#   print(letter)

#   def loop_over_string():
#     # Write your code here
#         name = "Damian"
#         for letter in name:
#             print(letter)
#         return name

# alphabet = 'abcdef'

# for letter in alphabet:
#   print(letter)


# for num in range(1, 10, 3):
#     print(num)


# Guide to Continue and Break in Python Loops#

# usernames = [
#     'John',
#     'damian',
#     'salvador',
#     'hervin',
#     'massimo'
# ]

# for name in usernames:
#     if us

# def loop_over_range():
#     for num in range(1, 11, 3):
#         print(num)


# print(loop_over_range())


# usernames = [
#     'John',
#     'damian',
#     'salvador',
#     'hervin',
#     'massimo'
# ]


# for name in usernames:
#     if name == "hervin":
#         print(f'Sorry, {name} you are not allowed')
#         continue
#     else:
#         print(f'{name} is allowed')

# John is allowed
# damian is allowed
# salvador is allowed
# Sorry, hervin you are not allowed
# massimo is allowed


# usernames = [
#     'John',
#     'damian',
#     'salvador',
#     'hervin',
#     'massimo'
# ]

# for name in usernames:
#     if name == "hervin":
#         print(f'{name} was found in at index {usernames.index(name)}')
#         break
#     print(name)
# # John
# # damian
# # salvador
# # hervin was found in at index 3


# vegetables = ["onion", "broccoli", "apple", "spinach"]
# for vegetable in vegetables:
#     if vegetable == "apple":
#         print(f'{vegetable} is not a vegetable')
#         break
#     print(vegetable)


# nums = list(range(1, 11))

# # for num in nums:
# #     print(num)

# while len(nums) > 0:
#     print(nums.pop())

# guessing game #

# def guessing_game():
#     while True:
#         print('what is yout guess?')
#         guess =  input()

#         if guess == '9':
#             print('Your correctly guessed it!')
#             return False
#         else:
#             print(f'No, {guess} is no the answer, please try again\n')

# guessing_game()


# def loop_using_while():
#     dog_house = ["isis", "terrance", "lil", "cooki"] 
#     counter = 0

#     while len(dog_house) > 0:
#         print(dog_house.pop())
#         counter += 1
    
    
#     return [dog_house, counter]
# loop_using_while()

# def loop_using_while():
#     counter = 0
#     dog_house = ["isis", "lily", "Terrance", "silvestre"] # Put dog names here
    
#     while len(counter < dog_house.len):
#         print(dog_house)
#         counter += 1
    
    
#     return [dog_house, counter]

# loop_using_while()


# def loop_using_while():
#     counter = 0

#     dog_house = ["isis", "lily", "Terrance", "silvestre"]
#     while len(dog_house) > counter:
#             print(dog_house[counter])
#             counter += 1
    
#     return [dog_house, counter]
# loop_using_while()


# How to Combine and Flatten 
# Lists in Python with the For / In Loop #

# legacy_customers = ['Damian', 'Ana']
# new_customers = ['Massimo', 'Salvador']

# for legacy_customer in legacy_customers:
#     new_customers.append(legacy_customer)

#     print(new_customers)


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [9, 7, 8, 4]

for list in list1:
    list2.append(list)

print(list2)