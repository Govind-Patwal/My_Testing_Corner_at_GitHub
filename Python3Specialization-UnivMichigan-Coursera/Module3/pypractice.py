# NOTE: requests is not a native python library
# if not installed, go to win cmd -> pip3 install requests
import requests 
import json

Base_URL = 'https://api.datamuse.com/words'  # Base URL before ?
search_parameter_dict = {'rel_rhy':'sun'} 
page = requests.get(Base_URL, params=search_parameter_dict)

py_object1 = page.json()
# print(py_object)

py_object2 = json.loads(page.text)

print(py_object1 is py_object2)
print(py_object1 == py_object2)




'''
the first thing for APIs is to get the url of the page where the APIs are listed
then import the requests module by import requests, and the jason module by import jspn

then talk to the server n a get response of your requests  server_response = requests.get(URL)


then check the urkoif the server response by server_response.url

to get the text response do a server_response.txt   the output is a string format ... to convert it into Python object do server_response.json()   or json.loads(server_response.txt) 
to read the pretty version of this json.dumps(server_response.txt, indent = 2)
the output of this can be see on the python screen on on a python editor



'''



