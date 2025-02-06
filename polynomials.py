
"""
This program helps you to factor polynomial expressions.

"""


import random

print ("hi welcome")
  
while True:
    """
        user_input = input("Enter a polynomial expression: ")
        # here we check if the user input is equal to a $, if so exit the loop
        if user_input == "$":
            break    
        print("You entered: ", user_input) 
    """
# make a random number between 1-3 that is an integer
    
    number_of_roots = random.randint(1, 4)
    print (number_of_roots)
    roots = []
    for i in range(number_of_roots):
        roots.append(random.randint(-10, 10))
    polynomial = ""
    if number_of_roots == 2:
        sum = roots[0] + roots[1]
        if sum < 0:
            if sum == -1:
                sum_string = '- x'
            else:
                sum_string = str(sum) + 'x'
        elif sum > 0:
            if sum == 1:
                sum_string = '+ x'
            else:
                sum_string = '- ' + str(sum) + 'x'
        else:
            sum_string = ''

        product = roots[0] * roots[1]
        if product < 0:
            product_string = '- ' + str(-product) 
        elif product > 0:
            product_string = '+ ' + str(product)
        else: 
            product_string = ''
        
        polynomial = f"x^2  {sum_string}  {product_string}"
        user_input = input(f"Factor the polynomial {polynomial}: ")
        if user_input == "$":
            break

    else:
        print("can't handle that right now")
    
  



#     """
# This program helps you to factor polynomial expressions.

# """


# import random

  
# while True:
#     """
#         user_input = input("Enter a polynomial expression: ")
#         # here we check if the user input is equal to a $, if so exit the loop
#         if user_input == "$":
#             break    
#         print("You entered: ", user_input) 
#     """
# # make a random number between 1-3 that is an integer
    
#     number_of_roots = random.randint(1, 4)
#     roots = []
#     for i in range(number_of_roots):
#         roots.append(random.randint(-10, 10))
#     polynomial = ""
#     if number_of_roots == 2:
#         sum = roots[0] + roots[1]
#         if sum < 0:
#             sum_string = '+ ' + str(sum)
#         elif sum > 0:
#             sum_string = '- ' + str(sum)
#         else:
#             sum_string = ''
#         product = roots[0] * roots[1]
#         polynomial = f"x^2  {sum_string}x  {product}"
#     else:
#         print("can't handle that right now")
    
#     user_input = input(f"Factor the polynomial {polynomial}: ")
#     if user_input == "$":
#         break
#     if number_of_roots == 2:
#         sum = roots[0] + roots[1]
#         product = roots[0] * roots[1]
#         polynomial = f"x^2 - {sum}x + {product}"
#     else:
#         print("can't handle that right now")
    
#     user_input = input(f"Factor the polynomial {polynomial}: ")
#     if user_input == "$":
#         break