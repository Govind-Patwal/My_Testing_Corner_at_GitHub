# # week 2

# # sequences - can be iterated, can be referenced using index, can be sliced
# # strings, lists, tuples

# print((3.12,) == 3.12)
# # b = (3,)
# # c = a + b
# # print(c)



# # b = a + ' but I am happy'
# # # c = str(b)
# # # d = ''.join(b)
# # print(b)

# week 3

# for _ in something # use _ when you are not using in the loop

# for can be used for sequences, lists, tuples, strings # called sequences, iterables

# i is called the for loop variable or iterator variable

# boolean - True or False (upper case)

# print(true)
# print(True)

# False = 0, 0.0 or ''
# True is any other int, float or str
# PEMDAS
# == < <= > >=
# not
# and or

# # usage of enumerate

# # assign values to varable
# text = 'the quick brown fox jumped over the lazy dog.'

# # GOAL - count the number of vowels in the sentence
# counter = 0
# for char in text:
#     if char in 'a' + 'eiou':
#         counter += 1

# # print the result
# print(counter)

# GOAL = finding the max value in a list


## loop over sequence/iterables

# to loop over its indexes == use 


# GOAL - find the number of words that have either a or e

# GOAL - find the number of words that have either a or e

# given list

# adding and deleting elements in a list
# GOAL: checking a string for palindrome

# Step1: enter a sentence
p_phrase = "was it a car or a cat I saw"

# Step2: reverse the sentence by converting to a list and then reversing the list
# Step 2a: convert the sentence to a list of words
p_phrase_to_list = list(p_phrase)
print(p_phrase_to_list)
# Step 2b: reverse the list
p_phrase_to_list.reverse()
# Step 2c: join the reversed list to form a sentence
r_phrase = ''.join(p_phrase_to_list)
print(r_phrase)







