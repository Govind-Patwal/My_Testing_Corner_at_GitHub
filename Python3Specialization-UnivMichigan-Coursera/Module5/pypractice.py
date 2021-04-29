import functools

list1 = ['this', 'is', 'the', 'thing']
str1 = ' '.join(list1)
print(str1)
print('----------------')
str2 = functools.reduce(lambda x,y: x+y, list1)
print(str1)