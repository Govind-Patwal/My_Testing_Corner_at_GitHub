# list of punctuation characters
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# strip punctuation from a string
def strip_punctuation(string1):
    for char in string1:
        if char in punctuation_chars:
            string1 = string1.replace(char, '')
    return string1

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# return the number of positive words in a string
def get_pos(string2):
    string3 = strip_punctuation(string2)
    string4 = string3.lower()
    
    word_list = string4.split()
    pos_words_so_far = 0    
    
    for word in positive_words:
        num_words = word_list.count(word)
        pos_words_so_far += num_words
    return pos_words_so_far

# return the number of negative words in a string
def get_neg(string2):
    string3 = strip_punctuation(string2)
    string4 = string3.lower()
    
    word_list = string4.split()
    neg_words_so_far = 0    
    
    for word in negative_words:
        num_words = word_list.count(word)
        neg_words_so_far += num_words
    return neg_words_so_far

# read the file project_twitter_data.csv as lines of strings
filepath = 'project_twitter_data.csv'
with open(filepath, 'r') as file_reference:
    lines = file_reference.readlines()
    # print(file_reference.read())   # view of original file - always good to see
    # input format -> 'tweet_text,retweet_count,reply_count\n@twitteruser...\n'
    
    list_before_converting_to_final_string = ['Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n']
    
    for line in lines[1:]:
        tot_positive_words = get_pos(line.strip())
        tot_negative_words = get_neg(line.strip())
        net_score = tot_positive_words - tot_negative_words
        
        # each line is a single string, need to convert it to list to pull values out 
        input_line_as_a_list_of_words = line.strip().split(',')    
        
        # required output format -> 'Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n...\n'
        string_to_append = '{},{},{},{},{}\n'.format(input_line_as_a_list_of_words[1],input_line_as_a_list_of_words[2],tot_positive_words,tot_negative_words,net_score)
        list_before_converting_to_final_string.append(string_to_append)
    
    # print(list_before_converting_to_final_string)
    final_string = ''.join(list_before_converting_to_final_string)
    # print(final_string)

filepath = 'resulting_data.csv'
with open(filepath, 'w') as file_reference:
    file_reference.write(final_string)
    
filepath = 'resulting_data.csv'
with open(filepath, 'r') as file_reference:
    print('==== Original File: 1 single string with \\n between lines, and comma(,) between values ===== \n', file_reference.read()  ) # this will print the entire file as 1 string, with \n denoting end of line
    lines = file_reference.readlines() # this will divide the file into 1 single list of strings - with each single string representing 1 line, ending in \n
    print('==== As a single list of strings, \\n seperating lines ==== \n',lines) # print the file above - 1 single list of strings\lines
    x_axis = []  # initialize x_axis
    y_axis = []  # initialize y_axis
    
    for line in lines[1:]:  # line is 1 single string with a \n at the end
        line_from_1_string_to_a_list_of_words = line.strip().split(',')
        # print ('==net score===')
        # print(line_from_1_string_to_a_list_of_words[4]) # line[4] is Net Score
        x_axis.append(int(line_from_1_string_to_a_list_of_words[4])) 
        # print ('==# of retweets===')
        # print(line_from_1_string_to_a_list_of_words[0]) # line[0] is Number of Retweets
        y_axis.append(int(line_from_1_string_to_a_list_of_words[0])) # line[0] is Number of Retweets 
        
print('========')
print('x_axis: ', x_axis)
print('y_axis: ', y_axis)