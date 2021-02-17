# pseudocode

# get the input from STDIN and store in str
my_string = input()

# convert str into a list using list(str)
str_as_list = list(my_string)

# iterate through the list and compare each alphabet with a list of vowels, accomplish this using list comprehension
vowel_in_string_list = [i for i in str_as_list if i in 'aeiouAEIOU']

# print the lenght of the list
no_of_vowels = len(vowel_in_string_list)
print(f'Number of vowel(s) in the string \"{my_string}\": {no_of_vowels}')
