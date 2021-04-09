import json
import requests

def paragraph_translator():
    '''
    This function asks the user for a paragraph, and returns a paragraph that has
    words with similar meanings. 
    '''
    input_paragraph = input('Please enter your paragraph: ')  

    input_para_as_words = input_paragraph.split()

    new_word_list = []

    for word in input_para_as_words:
        base_url = 'https://api.datamuse.com/words'
        query_parameters = {'ml':word, 'max':1}
        page_response = requests.get(base_url, params = query_parameters)
        py_object = json.loads(page_response.text)
        # print(json.dumps(py_object, indent=2))
        if len(py_object) == 0:
            new_word = word
        else:
            new_word = py_object[0]['word']
        
        new_word_list.append(new_word)
        
    new_paragraph = ' '.join(new_word_list)

    return new_paragraph

print('New Paragraph: {}'.format(   paragraph_translator() )