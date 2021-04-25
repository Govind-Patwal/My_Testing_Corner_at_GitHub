# # learning decorators in python

# # simple functions
# def return_object(object1): # return the same python object
#     return object1

# def shout (text): # returns the uppercase of a string
#     return text.upper()

# def whisper(text): # retunrs the lowercase of a string
#     return text.lower()

# # funcitons can be treated as objects, can be alised
# yell = shout 
# murmer = whisper 
# text1 = 'Govind Is My Name.'

# # function passed as an arguments
# print(return_object (text1))
# print(return_object( yell (text1) )) # passing function yell as an argument
# print(return_object( murmer(text1) )) # passing function yell as an argument

# # Returning functions from another functions.
# def outer_fn(object1):
#     def inner_fn(object2):
#         return object2 + '____' + object1
#     return inner_fn

# print(   (outer_fn('Govind'))('Patwal') *3  )

# outer_fn_var = outer_fn('Govind') # alternatively, creating a variable for the fn
# print(outer_fn_var('Patwal'))

# understand *args and **kwargs
# why ? to give more flexibility in terms of accepting the number of arguments

# def add_numbers(dict1):
#     sum = 0
#     for i in dict1:
#         sum += dict1[i]
#     return sum

# dict1 = {'s': 12, 'a': 13, 'p': 15}
# print(  add_numbers(dict1 )  )

# # concatenate_2.py
# def concatenate(**words):
#     result = ""
#     for arg in words.values():
#         result += arg
#     return result

# dict1 = {'s': 12, 'a': 13, 'p': 15}
# print(concatenate(dict1 ='12'))


# using both *args and **kwargs

def using_args_and_kwargs(var1, var2, *args, **kwargs):
    print('var1: {}'.format(var1) )
    # sum1 = 
    # print('sum of args: {}'.format(sum(args) ))

    print('var2: {}'.format(var2) )
    # sum1 = 
    # print('sum of args: {}'.format(sum(var2) ))

    print('args: {}'.format(args) )
    # sum1 = 
    print('sum of args: {}'.format(sum(args) ))

    print('kwgs: {}'.format(kwargs) )
    list1 = list(kwargs.values())
    kwargs_1_string = ' '.join (list(kwargs) )
    # print(list1)
    print('concat of keys of kwgs: {}'.format(kwargs_1_string) )
    print('sum of values of kwgs: {}'.format(sum(list1)) )


using_args_and_kwargs(1, 'String 1', 34,13,45,67,78, apples=34, balls=34, cats=36 )


