from decimal import Decimal  

#Python String Basics

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
#from decimal import Decimal calling from top

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



#Overview of Popular Math Functions in Python

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


#Guide to Nested Lists and Best Practices for Storing Multiple Data Types in a Python List



users = ['Damian', 'Massimo', 'Salvador', 'Walter', 'Jessy']

ids = [1, 2, 4]
countries = ["Colombia", "Spain", "Germany"]
users.append(countries)
mixed_list = [ids, users]
print(mixed_list)