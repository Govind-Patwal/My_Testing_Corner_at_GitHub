def test(var1, var2 = 'default', *args, **kwargs):
    print('var1: {}'.format(var1))
    print('var2: {}'.format(var2))
    print('args: {}'.format(args))
    print('kwargs keys: {}'.format(kwargs.keys()))
    print('kwargs values: {}'.format(kwargs.values()))

test('var1', 34, 23,23, a = 'test', var2=23)


    