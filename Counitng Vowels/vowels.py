#import pandas as pd

count = 0
string1 = input()
for word in string1:
    if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
        count += 1

print(count)


