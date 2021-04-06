list1 = ['usa', 'can', 'india']
print('list1: {}'.format(list1))
print('list2: {}'.format(list(map(lambda string1 : len(string1)*2, list1))))
print('list3: {}'.format(list(filter(lambda string1 : len(string1)*2, list1))))


