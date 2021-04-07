list1 = ['usa', 'can', 'india']
print('list1: {}'.format(list1))
print('list2: {}'.format(list(map(lambda string1 : len(string1)*2, list1))))
print('list3: {}'.format(list(filter(lambda string1 : len(string1) == 3, list1))))


print('map fn uisng list comprehension:  {}'.format([len(i)*2 for i in list1])   )
print('filter fn uisng list comprehension:  {}'.format(    [i for i in list1 if len(i) == 3 ]   ) ) 