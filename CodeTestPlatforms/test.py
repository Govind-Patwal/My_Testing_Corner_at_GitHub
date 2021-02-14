# enter the string from STDIN
# main_string = str(input())
main_string = 'the quick brown fox jumped over the lazy dog'

# enter the substring
substring = 'the'
# >>> the

# initialize count
count = 0
last_index = -1

# iterate over the main_string
for i in range(len(main_string)):
    if substring in main_string[i:]:
        current_index = main_string[i:].index(substring)
        if current_index != last_index:
            count += 1
            last_index = current_index

print(count)