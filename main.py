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
#We got inversal list


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
#We can store the variable with sorted with sort not

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

tags = ['pythons', 'javascript', 'tutorials']

# Nope

# tags[-1] = 'programming'
# print(tags) # This way remove the original list

# tags.extend('react')
# print(tags) # This way add the element separted


# tags.extend(['react'])
# print(tags) 
# ['pythons', 'javascript', 'tutorials', 'react']#

#Correct way to add


new_tag = tags + ['react']
tags.extend(['Damian'])

print(new_tag) 
# ['pythons', 'javascript', 'tutorials', 'react']#

print(tags)
# ['pythons', 'javascript', 'tutorials']#