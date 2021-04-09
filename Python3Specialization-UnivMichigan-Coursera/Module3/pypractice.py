# NOTE: requests is not a native python library
# if not installed, go to win cmd -> pip3 install requests
# import requests 
# import json

# Base_URL = 'https://api.datamuse.com/words'  # Base URL before ?
# query_parameter_dict = {'rel_rhy':'sun'} 
# page = requests.get(Base_URL, params=query_parameter_dict)

# py_object1 = page.json()
# # print(py_object)

# py_object2 = json.loads(page.text)

# print(py_object1 is py_object2)
# print(py_object1 == py_object2)

'''
the first thing for APIs is to get the url of the page where the APIs are listed
then import the requests module by import requests, and the jason module by import jspn

then talk to the server n a get response of your requests  server_response = requests.get(URL)


then check the urkoif the server response by server_response.url

to get the text response do a server_response.txt   the output is a string format ... to convert it into Python object do server_response.json()   or json.loads(server_response.txt) 
to read the pretty version of this json.dumps(server_response.txt, indent = 2)
the output of this can be see on the python screen on on a python editor

'''

# defining a function to find 10 rhyming words

# importing the requests and json modules
# import requests
# import json

# def similar_sounding_words():
#     '''
#     This function when invoked outputs a list of 5 words that sound like the inputted word
#     >>> similar_sounding_words("sun")
#     ["fun", "run", "gun", 'learn', 'son']
#     '''
#     word = input('Enter the word you want to find similar sounding words for: ')
#     max_input = input('Enter the number of results: ')

#     base_url = 'https://api.datamuse.com/words'
#     query_parameters = {'rel_rhy': word} # putting the value of word here
#     query_parameters['max'] = max_input  # specifying the number of results required

#     page = requests.get(base_url, params=query_parameters)
#     py_object = json.loads(page.text)

#     list_of_words = [level_1_dict['word'] for level_1_dict in py_object]

#     return list_of_words   

# print( similar_sounding_words() )

# print(help(similar_sounding_words))





# check you understanding of requests

# writing a ffunction to find 10 similar meaning words given a word, 
# also given is the website whose API is to be used - datamuse.com

# Step 1 - explore the website, find the enpoint page and the syntax
# end point = https://api.datamuse.com/words

# Step 2: find the query parameters
# similar meaning words - ml=something


# import json
# import requests

# def return_similar_meaning_words():
#     '''
#     This function asks the user for a word and the number of results requeired, 
#     and returns a number of sumilar meaning words
#     '''
#     input_word = input('Please enter the word: ')
#     number_of_results = int (  input('Enter the number of results requierd: '))

#     base_url = 'https://api.datamuse.com/words'
#     query_parameters = {'ml':input_word, 'max':number_of_results}

#     page_response = requests.get(base_url, params = query_parameters)
#     py_obj = json.loads(page_response.text)
#     pretty_view = json.dumps(py_obj, indent = 2)
#     three_word = py_obj[0]['word']

#     word_list = [dict_level1['word'] for dict_level1 in py_obj]
 
#     return word_list

# print(return_similar_meaning_words())



# import json
# import requests

# def paragraph_translator():
#     '''
#     This function asks the user for a word and the number of results requeired, 
#     and returns a number of sumilar meaning words
#     '''
#     input_paragraph = input('Please enter the word: ')

    

#     input_para_as_words = input_paragraph.split()

#     new_word_list = []

#     for word in input_para_as_words:
#         base_url = 'https://api.datamuse.com/words'
#         query_parameters = {'ml':word, 'max':1}
#         page_response = requests.get(base_url, params = query_parameters)
#         py_object = json.loads(page_response.text)
#         # print(json.dumps(py_object, indent=2))
#         if len(py_object) == 0:
#             new_word = word
#         else:
#             new_word = py_object[0]['word']
        
#         new_word_list.append(new_word)
        
#     new_paragraph = ' '.join(new_word_list)

#     return new_paragraph

# print('New Paragraph: {}'.format(   paragraph_translator() )  )

import json
import requests # not native to python: win cmd -> pip3 install requests
import requests_cache # not native to python: win cmd -> pip3 install requests_cache

requests_cache.install_cache()

# using some more parameters
# initiating cache: name = dict_in_py_memory
# location = python memory
# expiration = 600 seconds
# requests_cache.install_cache("dict_in_py_memory", backend="sqlite", expire_after=600)

def caching_check ():
    
    input_word = input('Enter the lookup word: ')
    input_number_of_results = int(input('Enter the number of desired results: '))
    query_parameters = {'ml':input_word}
    # sorted the dict with keys, this will lead to less get requests from the page, in case the keys are not in the right sequence
    sorted_query_parameters = { key:query_parameters[key] for key in sorted(query_parameters) }

    base_url = 'https://api.datamuse.com/words'
    page_response = requests.get(base_url, params=sorted_query_parameters)

    if page_response.from_cache:
        print('Great!!! The page was in Cache...')
        py_obj = page_response.json()
        word_list = [  dict_level1['word'] for dict_level1 in py_obj[:input_number_of_results]  ]
        return word_list
    else:
        print('We could NOT find the page in Cache...')
        py_obj = page_response.json()
        # Alternatively: py_obj = json.loads(page_response.text)
        word_list = [  dict_level1['word'] for dict_level1 in py_obj[:input_number_of_results]  ]
        return word_list

print(caching_check())

