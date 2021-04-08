# NOTE: requests is not a native python library
# if not installed, go to win cmd -> pip3 install requests
import requests 
import json

page = requests.get('https://www.google.com/search?q=govind+patwal')
# print(page)  # get the server response
# print(page.text[:100])  # get the text of the page (first 100 characters) as it will be in string format
print(json.loads(page.text))


'''
the first thing for APIs is to get the url of the page where the APIs are listed
then import the requests module by import requests, and the jason module by import jspn

then talk to the server n a get response of your requests  server_response = requests.get(URL)


then check the urkoif the server response by server_response.url

to get the text response do a server_response.txt   the output is a string format ... to convert it into Python object do server_response.json()   or json.loads(server_response.txt) 
to read the pretty version of this json.dumps(server_response.txt, indent = 2)
the output of this can be see on the python screen on on a python editor



'''



