def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

myfunc(2)(11)