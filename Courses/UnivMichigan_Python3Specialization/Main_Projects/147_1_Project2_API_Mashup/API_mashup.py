import json
import requests
import requests_cache

def get_movies_from_tastedive(movie_name): # takes a movie name as input
    endpoint_url = 'https://tastedive.com/api/similar'
    query_params = {}
    query_params['limit'] = 5
    query_params['q'] = movie_name
    query_params['type'] = 'movies'
    sorted_params = query_params
    page_response = requests.get(endpoint_url, params=sorted_params )
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
    return big_list_of_related_movies # 1 big list of movie titles, non duplicate

################################################

def get_movie_data(movie_title): # movie name
    endpoint_url = 'http://www.omdbapi.com/'
    query_params = {}
    query_params['t'] = movie_title
    query_params['r'] = 'json'
    # sorted_params = {key:query_params[key] for key in sorted(query_params) }
    sorted_params = query_params
    page_response = requests.get(endpoint_url, params=sorted_params)
    page_py_object = page_response.json()
    return page_py_object # dict with related info

def get_movie_rating(OMDB_dict): # OMDB movie list
    movie_ratings = OMDB_dict['Ratings']
    for rating in movie_ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            desired_rating = int(rating['Value'].split('%')[0]   )
        else:
            desired_rating = 0
        # print(desired_rating)
    return desired_rating # Rotten tomatoes rating of the movie

def get_sorted_recommendations(list_of_movie_titles):
    combined_list_of_5_titles_per_movie = get_related_titles(list_of_movie_titles)
    movies_with_ratings = {}
    for title in combined_list_of_5_titles_per_movie:
        OMDB_title1 = get_movie_data(title)
        Movie_Rotten_rating = get_movie_rating(OMDB_title1)
        movies_with_ratings[title] = Movie_Rotten_rating
        
    print(movies_with_ratings) 
    sorted_list = sorted(movies_with_ratings, key=lambda key : - movies_with_ratings[key], reverse = True )
    print(sorted_list)
    return sorted_list
        
get_sorted_recommendations(   ['Black Panther', 'Sherlock Holmes']    )

