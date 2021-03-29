'''
https://www.coursera.org/learn/python-functions-files-dictionaries?specialization=python-3-programming
This course introduces the dictionary data structure and user-defined functions. You’ll learn about local and global variables, optional and keyword parameter-passing, named functions and lambda expressions. You’ll also learn about Python’s sorted function and how to control the order in which it sorts by passing in another function as an input. For your final project, you’ll read in simulated social media data from a file, compute sentiment scores, and write out .csv files. It covers chapters 10-16 of the textbook “Fundamentals of Python Programming,” which is the accompanying text (optional and free) for this course.
The course is well-suited for you if you have already taken the "Python Basics" course and want to gain further fundamental knowledge of the Python language. Together, both courses are geared towards newcomers to Python programming, those who need a refresher on Python basics, or those who may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.
This is a follow-up to the "Python Basics" course (course 1 of the Python 3 Programming Specialization), and it is the second of five courses in the specialization.
'''
# # #Reading a file natively in Python

# # open the file
# fileref = open('election_results.csv', 'r')

# # --------------------------------------------------
# # -------- .read(): reads the entire file as 1 string
# # --------------------------------------------------

# contents = fileref.read()
# print(contents)

# # read first 50 characters of the file into 1 string
# contents = fileref.read()
# print(contents[:50])

# # --------------------------------------------------
#  -------- .readlines(): reads the file as 1 list, with every line as a string
# # --------------------------------------------------

# lines = fileref.readlines()
# print(lines)

# # read first 50 lines: 1 list of 50 strings (each line is a string)
# lines = fileref.readlines()
# print(lines[:50])

# # read first 50 lines in 50 lines: 1 list of 50 strings (each line is a string)
# # this will display the lines with a gap of one line between them
# lines = fileref.readlines()
# for line in lines[:50]:
#     print(line)

# # removing the space between two lines, use the string.strip() method or 
# # # print(line, end='') 
# lines = fileref.readlines()
# print(len(lines))
# for line in lines[:50]:
#     print(line.strip())  # or print(line, end='')

# fileref = open('../Data/election_results.csv', 'r') # this will load the file at a location
# # reading the file as 1 single string
# entire_file_as_lines = fileref.readlines()  
# # print(entire_file_as_string)
# # printing the lines of the file
# for line in entire_file_as_lines[:50]:
#     print(line)

# # # for readign lines: ourput will be 1 list with each line as a string
# lines = fileref.readlines()    
# # print all the lines
# print(lines)
# # # printing each line one by one
# for line in lines:
#     print(line)

# # # print first 100 rows
# for line in lines[:100]:
#     print(line)

# # close the file
# fileref.close()

# file_obj = open('times_4.txt', 'w')
# for i in range(13):
#     file_obj.write(str(i*4) + '\n')
# file_obj.close()

# file_ref = open('times_4.txt', 'r')

# string = file_ref.read()

# print(string)

# file_ref.close()

# # using with

# with open('times_4.txt', 'r') as file_ref:
#     file_as_lines = file_ref.readlines()
#     for line in file_as_lines:
#         print(line.strip())


# receipe for reading and proressing a file

# filename = 'Data/election_results.csv'
# with open(filename, 'r') as file_ref:
#     file_as_lines = file_ref.readlines()
#     # assign value to header_row
#     header = file_as_lines[0]
#     # print header row
#     print(' ======   Header   ======= ')
#     print(header)
#     # find the records of the file
#     print('====== Records =====')
#     records = file_as_lines[1:]
#     number_of_records = len(records)
#     print('The number of records = {}'.format(number_of_records))
#     print('=====print the first 5 records')
#     print(records[:5])
#     print(' ====== print the first 50 records in a format')
#     for record in records[:50]:
#         record_as_list = record.split(',')
#         print('The Ballot {} in County {} was voted for {}'.format(record_as_list[0], record_as_list[1], record_as_list[2]), end ='')

# writing contents to a csv file

# given headers
# Name,Age,Sport

# given data
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

with open('olympian.csv', 'w') as file_ref:
    Header = '"Name","Age","Sport"'
    file_ref.write(Header + '\n')

    # write records
    for olympian in olympians:
        row_string = '"{}","{}","{}"'.format(olympian[0], olympian[1], olympian[2])
        file_ref.write(row_string +'\n')

filename = 'olympian.csv'
with open(filename, 'r') as file_ref:
    for line in file_ref:
        print(line, end='')        
    





