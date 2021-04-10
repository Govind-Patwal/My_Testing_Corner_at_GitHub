import json
import requests # not native to python: win cmd -> pip3 install requests
import requests_cache # not native to python: win cmd -> pip3 install requests_cache

requests_cache.install_cache()
'''
OTHER ARGUMENTS: requests_cache.install_cache(<file_name>, location = <>, expiration = <>)
# EXAMPLE
>>> requests_cache.install_cache(dict_in_py_memory, location = memory, expiration = 600)
# name = cache(default), dict_in_py_memory
# location = sqlite (default), memory, redis, mongodb   
# expiration = indefinitely(default), 600 seconds
1) https://geektechstuff.com/2020/06/28/caching-requests-python/
2) https://medium.com/@jasonrigden/requests-cache-library-tutorial-bceb400f1a01
3) https://requests-cache.readthedocs.io/en/latest/api.html
'''

def caching_check ():
    '''
    This function asks user for a word, and the number of words required that have the same meaning as the initial word, it also checks if the data was fethced from Cache
    >>> Enter the lookup word: run
    >>> Enter the number of desired results: 4
    Great!!! The page was in Cache...
    ['jump', 'walk', 'progress', 'fast walk']
    '''
     
    input_word = input('\nEnter the lookup word: ')
    input_number_of_results = int(input('Enter the number of desired results: '))
    query_parameters = {'ml':input_word}
    # sorted the dict with keys, this will lead to less get requests from the page, in case the keys are not in the right sequence
    sorted_query_parameters = { key:query_parameters[key] for key in sorted(query_parameters) }

    base_url = 'https://api.datamuse.com/words'
    page_response = requests.get(base_url, params=sorted_query_parameters)

    if page_response.from_cache:
        print('\nGreat!!! The page was in Cache...')
    else:
        print('\nWe could NOT find the page in Cache...')

    py_obj = page_response.json()
    # Alternatively: py_obj = json.loads(page_response.text)
    word_list = [  dict_level1['word'] for dict_level1 in py_obj[:input_number_of_results]  ]
    print('\nBelow is a List of {} words similar to {}:'.format(input_number_of_results, input_word)   )
    return word_list

print(caching_check())

