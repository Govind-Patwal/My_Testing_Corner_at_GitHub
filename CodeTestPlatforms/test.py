def mul_by_3(x):
    return x * 3

def single_call(fn, arg):
    return fn(arg)

def double_call(fn, arg):
    return fn(fn(arg))

print(   mul_by_3(2), single_call(mul_by_3, 2), double_call(mul_by_3, 2)    )