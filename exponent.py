from functools import reduce


def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total
    
# def manual_exponent(num, exp):
#     computed_list = [num] * exp
#     return(reduce(lambda total, element: total * element, computed_list))

    print(manual_exponent(2, 3))
    print(manual_exponent(10, 2))


