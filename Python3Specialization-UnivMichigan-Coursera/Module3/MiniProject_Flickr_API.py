import json
import requests
import requests_cache
import webbrowser

requests_cache.install_cache('flickr_cache')

def flickr_photo_retrival ():
    '''
    This function gets 2 inputs from the user
    1) image to search
    2) number of images
    It then calls Flickr API and returns results in JSON format
    It also opens 5 or less images in brower

    >>> Enter the tags as CSV: book
    >>> Enter the number of results required: 5

    *** We did NOT find the results in the Cache ... ***

    Matching URL # 1 is https://www.flickr.com/photos/58206214@N03/51106807379
    Matching URL # 2 is https://www.flickr.com/photos/191609161@N04/51107057946
    Matching URL # 3 is https://www.flickr.com/photos/29848963@N03/51106471637
    Matching URL # 4 is https://www.flickr.com/photos/162694074@N06/51107021646
    Matching URL # 5 is https://www.flickr.com/photos/34176693@N06/51106991306

    *** Opening the first 5 images in the brower ***
    '''

    tags_as_CSV = input('\nEnter the tags as CSV: ')
    desired_number_of_results = int(input('Enter the number of results required: '))

    base_url = 'https://api.flickr.com/services/rest/'

    # adding query params to a dict
    query_params = {}
    query_params['api_key'] = '7f62e659a47c2ddd0c2631d012eb8119'
    # query_params['per_page'] = desired_number_of_results
    query_params["tag_mode"] = "all"
    query_params["method"] = "flickr.photos.search"
    query_params['tags'] = tags_as_CSV
    query_params["media"] = "photos"
    query_params['format'] = 'json'
    query_params['nojsoncallback'] = 1

    # sorting the dictionary - will result in efficient caching and retrieval
    sorted_params = { key:query_params[key] for key in sorted(query_params) }

    # getting the page response
    page_response = requests.get(base_url, params=sorted_params)

    # printing the page response and URL
    # print(page_response)
    # print(page_response.url)

    # converting to a python object
    py_obj = page_response.json()
    # print(type(py_obj))

    # # pretty printing the py object
    # print(json.dumps(py_obj, indent =2))

    if page_response.from_cache:
        print('\n*** We found the results in the Cache ... ***\n')
    else:
        print('\n*** We did NOT find the results in the Cache ... ***\n')

    # results
    for idx, item in enumerate( py_obj['photos']['photo'][:desired_number_of_results] ) :
        print('Matching URL # {} is https://www.flickr.com/photos/{}/{}'.format((idx+1), item['owner'], item['id']   )  )

    # displaying the first 5 images in browser
    print('\n *** Opening the first 5 images in the brower ***\n')
    for item in py_obj['photos']['photo'][:5]  :
        url = 'https://www.flickr.com/photos/{}/{}'.format(item['owner'], item['id']   )  
        webbrowser.open(url)

flickr_photo_retrival()

print(help(flickr_photo_retrival))













