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

# read the file project_twitter_data.csv
filepath = 'project_twitter_data.csv'
with open(filepath, 'r') as file_reference:
    lines = file_reference.readlines()
    file_to_save = []
    file_to_save.append('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n')
    for line in lines[1:]:
        tot_positive_words = get_pos(line.strip())
        tot_negative_words = get_neg(line.strip())
        net_score = tot_positive_words - tot_negative_words
        # input line format
        # 'text of a tweet,the number of retweets,number of replies to that tweet'
        input_line_as_a_list_of_words = ( line.strip() ).split(',')
        # this will result in
        # ['text of a tweet','the number of retweets','number of replies to that tweet']
        
        # header of the output file
        # 'Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n'
        string_to_append = '{},{},{},{},{}\n'.format(input_line_as_a_list_of_words[1],input_line_as_a_list_of_words[2],tot_positive_words,tot_negative_words,net_score)
        file_to_save.append(string_to_append)

    for line in file_to_save:
        print(line)

filepath = 'resulting_data.csv'
with open(filepath, 'w') as file_reference:
    file_reference.write(file_to_save)