# An inner_function can be called with the syntax `outer_function()()` if
# it returns its name at the same indentation as its definition ...def inner_f(): 
# \n code... \n return inner_f (at the same indention as def inner_f()) 


def outer_f(fn_to_be_decorated):
    def wrapper(*args):
        return fn_to_be_decorated(*args)
    return wrapper


'''
def external_function():
    print('I am the external fn')
# outer_f(external_function)()
external_function = outer_f(external_function)
'''

@outer_f
def add_2(*args):   #same as outer_f(add_2)(*args)
    return sum(args)

var1 = add_2(23, 23, 23)
print(var1)

print(outer_f(add_2)(23, 23, 23))

