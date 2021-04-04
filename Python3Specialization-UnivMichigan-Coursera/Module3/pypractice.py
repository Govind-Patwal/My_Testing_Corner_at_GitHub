'''
University of Michigan
Python 3 Specialization
Course 3
Data Collection and Processing with Python
'''



d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

import json

string1 = json.dumps(d, indent=True)
print(string1)
