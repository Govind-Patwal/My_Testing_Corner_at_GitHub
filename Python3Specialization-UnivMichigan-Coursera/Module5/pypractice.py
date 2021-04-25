# learning decorators in python

import functools
result = functools.reduce( (lambda x,y : x + y), [ 12, 65, 2324, 78989])
print(result)