def foo(var1, var2):
    # crating a copy of variables to changing __main__ variables
    var1 = var1.copy()
    print('List before mutation inside the function: {}'.format(var1))
    # print(id(var1))
    var1.append(89)
    print('List after mutation inside the function: {}'.format(var1))

x,y = [21, 23],45
print('List in __main__ before function call: {}'.format(x))

# print('Id of original x: {}'.format( id(x)) ) 
foo(x,y)

print('List in __main__ after function call: {}'.format(x))
