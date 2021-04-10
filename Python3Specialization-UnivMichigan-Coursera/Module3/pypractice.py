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

# import json
# import requests # not native to python: win cmd -> pip3 install requests
# import requests_cache # not native to python: win cmd -> pip3 install requests_cache

# requests_cache.install_cache()
# # in the above, the default file name is cache, the default backend is sqlite

# # using some more parameters
# # name = default is 'cache'
# # location = default is 'sqlite'
# # expiration = default is indefinitely, 
# # requests_cache.install_cache("dict_in_py_memory", backend="sqlite", expire_after=600)

# def caching_check ():
    
#     input_word = input('\nEnter the lookup word: ')
#     input_number_of_results = int(input('Enter the number of desired results: '))
#     query_params = {'ml':input_word}
#     # sorted the dict with keys, this will lead to less get requests from the page, in case the keys are not in the right sequence
#     sorted_query_parameters = { key:query_parameters[key] for key in sorted(query_parameters) }

#     base_url = 'https://api.datamuse.com/words'
#     page_response = requests.get(base_url, params=sorted_query_parameters)

#     if page_response.from_cache:
#         print('\nGreat!!! The page was in Cache...')
#         py_obj = page_response.json()
#         word_list = [  dict_level1['word'] for dict_level1 in py_obj[:input_number_of_results]  ]
#         return word_list
#     else:
#         print('\nWe could NOT find the page in Cache...')
#         py_obj = page_response.json()
#         # Alternatively: py_obj = json.loads(page_response.text)
#         word_list = [  dict_level1['word'] for dict_level1 in py_obj[:input_number_of_results]  ]
#         return word_list

# print(caching_check())

# # importing modules
# import json
# import requests
# import requests_cache

# # installing cache and naming it
# requests_cache.install_cache('apple_cache')

# # creating the base url and query params
# base_url = 'https://itunes.apple.com/search'
# query_params = {'term': 'Ann Arbor', 'entity':'podcast'}
# sorted_query_params = {  key:query_params[key] for key in sorted(query_params)  }

# # getting the page response and converting to a py object
# page_response = requests.get(base_url, sorted_query_params)
# py_object = page_response.json()

# # checking if the page was retrieved from Cache
# if page_response.from_cache:
#     print('\n*** Was result in Cache? : YES ***\n')
# else:
#     print('\n*** Was result in Cache? : NO ***\n')

# ## viewing the py object in a prettier way
# # pretty_format = json.dumps(py_object, indent = 2)
# # print(pretty_format)

# ## print out the names of all the podcasts returned

# names_of_podcast = [dict1['trackName'] for dict1 in py_object['results'] ]
# print(names_of_podcast)


# import json
# import requests
# import requests_cache
# import webbrowser

# requests_cache.install_cache('flickr_cache')

# def flickr_photo_retrival ():

#     tags_as_CSV = input('\nEnter the tags as CSV: ')
#     desired_number_of_results = int(input('Enter the number of results required: '))

#     base_url = 'https://api.flickr.com/services/rest/'

#     # adding query params to a dict
#     query_params = {}
#     query_params['api_key'] = '7f62e659a47c2ddd0c2631d012eb8119'
#     # query_params['per_page'] = desired_number_of_results
#     query_params["tag_mode"] = "all"
#     query_params["method"] = "flickr.photos.search"
#     query_params['tags'] = tags_as_CSV
#     query_params["media"] = "photos"
#     query_params['format'] = 'json'
#     query_params['nojsoncallback'] = 1

#     # sorting the dictionary - will result in efficient caching and retrieval
#     sorted_params = { key:query_params[key] for key in sorted(query_params) }

#     # getting the page response
#     page_response = requests.get(base_url, params=sorted_params)

#     # printing the page response and URL
#     # print(page_response)
#     # print(page_response.url)

#     # converting to a python object
#     py_obj = page_response.json()
#     # print(type(py_obj))

#     # # pretty printing the py object
#     # print(json.dumps(py_obj, indent =2))

#     if page_response.from_cache:
#         print('\n*** We found the results in the Cache ... ***\n')
#     else:
#         print('\n*** We did NOT find the results in the Cache ... ***\n')

#     # results
#     for idx, item in enumerate( py_obj['photos']['photo'][:desired_number_of_results] ) :
#         print('Matching URL # {} is https://www.flickr.com/photos/{}/{}'.format((idx+1), item['owner'], item['id']   )  )

#     # displaying the first 5 images in browser
#     print('\n *** Opening the first 5 images in the brower ***\n')
#     for item in py_obj['photos']['photo'][:5]  :
#         url = 'https://www.flickr.com/photos/{}/{}'.format(item['owner'], item['id']   )  
#         webbrowser.open(url)

# flickr_photo_retrival()


import json
import requests_with_caching as requests

def get_movies_from_tastedive(movie_name): # takes a movie name as input
    base_url = 'https://tastedive.com/api/similar'
    query_params = {}
    query_params['limit'] = 5
    query_params['q'] = movie_name
    query_params['type'] = 'movies'
    sorted_params = query_params
    page_response = requests.get(base_url, params=sorted_params )
    py_object = page_response.json()
    return py_object  # dictionary that has all info about 5 related movies

def extract_movie_titles(movie_dict):  # dictionary that has all info about 5 related movies
    movie_title_list = [ title['Name'] for title in movie_dict['Similar']['Results'] ]
    return movie_title_list  # list of the movie titles

def get_related_titles(list_of_movie_titles): # list of the movie titles
    big_list_of_related_movies = []
    for item in list_of_movie_titles:
        movie_py_dict = get_movies_from_tastedive(item)
        movie_list = extract_movie_titles(movie_py_dict)
        for movie1 in movie_list:
            if movie1 not in big_list_of_related_movies:
                big_list_of_related_movies.append(movie1)
    return (big_list_of_related_movies) # 1 big list of movie titles, non duplicate

################################################

def get_movie_data(movie_title): # movie name
    baseurl = 'http://www.omdbapi.com/'
    query_params = {}
    query_params['t'] = movie_title
    query_params['r'] = 'json'
    # sorted_params = {key:query_params[key] for key in sorted(query_params) }
    sorted_params = query_params
    page_response = requests.get(baseurl, params=sorted_params)
    page_py_object = page_response.json()
    return page_py_object # dict with related info

def get_movie_rating(OMDB_dict): # OMDB movie list
    movie_ratings = OMDB_dict['Ratings']
    for rating in movie_ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            desired_rating = int(rating['Value'].split('%')[0]   )
        else:
            desired_rating = 0
        print(desired_rating)
    return desired_rating # Rotten tomatoes rating of the movie

def get_sorted_recommendations(list_of_movie_titles):
    combined_list_of_5_titles_per_movie = get_related_titles(list_of_movie_titles)
    movies_with_ratings = {}
    for title in combined_list_of_5_titles_per_movie:
        OMDB_title1 = get_movie_data(title)
        Movie_Rotten_rating = get_movie_rating(OMDB_dict1)
        movies_with_ratings[title] = Movie_Rotten_rating
        
    return movies_with_ratings
        
print(get_sorted_recommendations(   ['Venom']    ))














