list1 = [i for i in range (10,30)]

print(list1)

list2 = [i for i in list1 if i%2 == 1]

print(list2)

x = lambda x,y,z:x+y**4+z

print(x(12,1,0))
# print(x)