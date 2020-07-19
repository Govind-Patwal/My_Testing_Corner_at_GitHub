# A small funcion that asks the user for a string and return the count of vowels in it

# Initializing the vowel count to 0
vowel_count = 0

# Prompting the user for input
print("Please enter your text below: ")

# Store the inputted string
user_input = input()
for word in user_input:
    if word in "aeiouAEIOU":
        vowel_count += 1

# Print
print(f"The total number of vowels in the text that your entered are {vowel_count}.")