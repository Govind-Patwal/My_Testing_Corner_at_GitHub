'''
University of Michigan
Python 3 Specialization
Course 3
Data Collection and Processing with Python
'''



lst = [100, [169, 196, 1], 289, 324, 361]
copied_lst1 = lst[:]
copied_lst2 = lst*1
copied_lst3 = lst.copy()

print('original_lst: {}'.format(lst))
print('copied_lst1 using lst[:] : {}'.format(copied_lst1))
print('copied_lst1 using lst*1 : {}'.format(copied_lst2))
print('copied_lst1 using lst.copy() : {}'.format(copied_lst3))

lst[1].append('new element')

print('=======after adding a new element to the original list =============')
print('original_lst: {}'.format(lst))
print('copied_lst1 using lst[:] : {}'.format(copied_lst1))
print('copied_lst1 using lst*1 : {}'.format(copied_lst2))
print('copied_lst1 using lst.copy() : {}'.format(copied_lst3))

