import json
import requests # not native to python: win cmd -> pip3 install requests
import requests_cache # not native to python: win cmd -> pip3 install requests_cache

'''
# initiating cache: name = dict_in_py_memory
# location = sqlite, default, others 
# expiration = 600 seconds
1) https://geektechstuff.com/2020/06/28/caching-requests-python/
2) https://medium.com/@jasonrigden/requests-cache-library-tutorial-bceb400f1a01
'''
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