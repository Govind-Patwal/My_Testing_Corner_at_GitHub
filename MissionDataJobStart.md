# Mission Data Job Start 
### Target (Initial) - Job in 24 Wks (by June 17, 2021)
### Target (Revision 1) - Job in 32 Wks (by Aug 17, 2021)

---

### [POA](#POA) - My Plan of Action
### [Daily Activities](#Daily_Activity) - WBS - breaking POA into daily activities

### [Cheat Sheet](#Cheat_Sheet) - Learning during this journey

### [Job Search Keywords](#Job_search_keywords) - Job Search Keywords
### [Good Links](#Good_Links) - Good links for reference

### [Project Ideas](#Project_Ideas) - Project Ideas

---

### POA

Part 1 | Part 2
| --- | --- |
Hard Skills: Product improvment | Soft Skills: Marketing and Sales
After inital setup: ONLY on Weekends | After inital setup: ONLY on Weekdays
Kaggle(python_pandas) + Django + Kaggle(remaining modules) + Canvas (in class + GitLab) + KaggleCourseAgain + Kaggle Competitions + own projects + resources section (on my portfolio website) + videos  | Part 1: (Finding new ones) and Part 2: (Retaining) - RecruitmentAgencies + JobSupportGroups (Govt) + JobPortals + DirectCompanies + Internships + Notifications + Sharing on LinkedIn

---




1. Python
    - Google Python Class - https://developers.google.com/edu/python
    - UofT Bootcamp exercises
    - UofT GitLab exercises
    - YouTube
2. Django / Flask

3. PostgreSQL standalone
    - all read/write SQL functions from Python 

4. AWS 
    - all read/write AWS functions from Python, using PostgreSQL DB

5. HTML website - inputting a text, calling AWS, running Python on AWS...

6. Machine Learning + Deep Learning

7. Tableau 
---
### Daily_Activity
Wk starts on a Monday and ends on a Sunday

Wk | Dates | Planned | Executed | Evaluation
| --- | --- | --- | --- | --- |
0 | 2020/12/07 - 2020/12/13 | This Wk: Demo day + Relaxation | Bootcamp finished last Sunday (12/06) ## 1st 4 days of this week spent on Practicing for Demo day on Dec/10/2020. ## Sat/Sun spent relaxing | 
1 | 2020/12/14 - 2020/12/20  | Google's Python Class + laptop setup | New Laptop delivered on 12/14, Setting up new Laptop, partitioning (created D: for non-OS), Installing Git, Python, Anaconda - checking for opening .ipynb files from outside D:, copying files from oustside. ## Started Google Python class, found it was Python 2, so dropped this plan - found more courses on python.org, and W3 schools, but decided to go through UofT Bootcamp modules again ## Spent time on ways to create Video with Green backgound so that I could create educational videos and put on GitHub - tried Zoom, Logitech Capture, Logitech Gaming, OBS, Chroma Cam , Personify. ## Started with Bootcamp Python, moved to working on Career Service tasks - finished the intro, now working on others parts, decided to use the next 2 Wks to complete all tasks related to becoming Employee Ready and Employee Competitive and then revisit Hard/Soft Skills| Plan changed mid-wk
2 | 2020/12/21 - 2020/12/27  | Complete tasks to become Employer-Ready | Change of plans - to Exercise everyday, am willing to push the Job start date by 2-4 months to achieve this. Completed first draft of brand statement, resume and LinkedIn on time | 100% completed ##talked to career director (1st time)
3 | 2020/12/28 - 2021/01/03 | Complete portfolio - GitHub Pages | Completed Portfolio on GitHub Pages ## Started Kaggle Python course - https://www.kaggle.com/learn/python ## Year End and New Year Celebrations
4 | 2020/01/04 - 2021/01/10 |  | ## RBC internship assessment ## Jan 10 - received Kaggle certificate of completion - Python
5 | 2020/01/11 - 2021/01/17 |  | ## got feedback from CareerServices Team, implemented feedback ##submitted application for 'data analytics specialist' on gojobs.gov.on.ca form ##started Ontario Internship form ## applied TDSB Can-Ex ## edX University of Texas query ## wrote to UofT MScAC team ##resolved medicine issue
6 | 2020/01/18 - 2021/01/24 |  | ## 2nd feedback from CareerService Team, implemented and became Employer-ready ##talked to career director (2nd time) ## CALC Can-Ex writing, speaking, infosession ## career services event ## submitted Ontario Internship form ## Kaggle Pandas: 1-3
7 | 2020/01/25 - 2021/01/31 |  | 
8 | 2020/02/01 - 2021/01/07 |  |  
---

### Cheat_Sheet
**Credits**
- https://www.kaggle.com/learn/overview

Number | Action | Shortcut
|---|---|---|
1 | Checking the version of Python in Windows | cmd -> type `python --version`
2 | Running a python file | cmd -> cd to the root where file is placed -> python <filename>
3 | Opening a .pynb file in D: | open Anaconda prompt -> d: -> jupyter notebook
4 | **Kaggle Course - 1/18** | **Python - https://www.kaggle.com/learn/python**
4a | 3 VERY important functions in python | >>> `type()` (what's type is this object?), >>> `dir()` (what can I do with it) >>> `help()` (tell me more about it)
4b | print in python | print(x), help(print), print(x, end =' ' )
5 | operators | [+ - * /],   11 % 3 = 3 (% is Modulus or reminder of division), 11 // 3 = 2 (// Floor division), 2**3 = 8, -3
6 | PEMDAS | Parentheses, Exponent, Multiplication, Division, Addition, Subtraction
7 | Python built-in function | min(1,5,6,7,8) , max(1,2,4,65), abs(-34)
8 | Convert to int, float, str, bool | x = int('223') OR float(10) OR str(10) OR bool(10)...for bool, only the number 0 is False, for strings only empty string is False (even a whitespace is TRUE)...check the outpur using type(x)
9 | help with a function | help(function_name), eg `help(print)`
10 | defining a function | def <functiion_name>(parameters): code_text return <value_to_be_returned>
10a | return | it will break out of the current function, can be used to return if all other options have been exausted wihtout any outcome
10b | : and indentation | very important in python
11 | commenting a line | #
12 | ***Docstrings*** Good Programming practice | It is a triple-quoted string (can span multiple lines) and it comes right below after a function has been named. When we call help() on that function, it shows the docstring. eg  `""" This is a description of the function above >>> """`
13 | Higher order functions | functions that operate on other functions
14 | 'pass' is a placeholder code  | it can be used inside a function when there is no code, when only the function name is known and zero code has been written  def function_name(): pass
15 | rounding a float | round (number, ndigits) ... default ndigits = 0, it can be negative, it will round to hundreds, tens, thousands
16 | having a default argument in a function | `def function_name(x, y=3):` ...
17 | Boolean operators | True or False
18 | Boolean operators | ==, !=, <=, >=, <, > 
19 | Boolean expression | `and`, `or`, `not`
19a | Boolean operator precedence | in the absence of a parenthesis,`and` is evaluated before `or`
20 | Combining Boolean operators | True and True = True, True and False = False, True or True = True, True or False = True
21 | Conditionals | if <boolean_conditional>:, elif <boolean_conditional>:, else:
22 | what about `if 0:` | python treats this as `if False:` similarly `if '':` is False and `if 1:` or `if 'str':` = True
23 | Lists - help(list) | Lists are ordered sequences of values, they are mutable (length and values can be changed). Items in the list can be numbers, strings, lists, variables, or a combination, when no elements are mentioned, it is a empty list
24 | Indexing | indexing starts at zero, so the first element is [0]...indexing ends at -1 so the last element is [-1] ... the list can be accessed in many ways from [0, ..., -1]
25 | Slicing a list (it is treated as a list) | First n elements = list_name[:n], last n elements = list_name[-n:], all elements = list_name[:] Or list_name....when calling list[m:n], it starts from the element at index m...to the element at index (n-1), so list[4:7] will show elements at index 4 to index 6 = 3 elements
26 | Changing lists | simple reassignment, list[n][m] = []
27 | Lenght of a list | len(list_name)
28 | Sorting a list in ascending order | sorted(list_name)
29 | Sum, Min, Max of elements in a list | sum(list), min(list), max(list)
. | Making a complex number | c = 12 + 3j   (the key is j, nothing else will work), printing the imaginary part of c, print(c.imag)
31 | List methods - adding 1 element to the end of the list | `list.append('')` appends ONLY 1 element to the end of the list, the 1 element could be number, string, or a list
32 | List - remove the last element of the list | `list.pop()`, this will remove the last element and return the last element
33 | Returing index of the first occurane of an element in list | `<list_name>.index(<element>)`
34 | checking element in a list | `<element> in <list_name>`
35 | Tuples - help(tuple) | Tuples are just like lists. Difference - created using () OR without any opening/clsing brackets AND at least 2 elements - e.g. `<tuple> = <element1>, <element2>` , and are immutable. HOWEVER - The lists inside the tuples are mutable.
36 | Tuples are often used for functions that have multiple return values | for example, the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple, which can be assigned to a tuple/list ....finally it can also be used for swapping two variables  `a = 1` `b= 0` `a,b = b,a` `print(a,b)`
37 | Loops | to repeteatedly execute some code
38 | for loop | can be used to loop over list, tuple, strings (a string is treated as a tuple)
39 | misc | to check if a char is upper/lower case `'P'.isupper()`
40 | range () | A very important function similar to for (i, i<10, i++) in C++. This allows for the code to run for a required number of times. `for i in range(10):` ... also comes in handy as you can have the range equal to the length of a list
41 | while loop | be very careful about (1) increasng the counter at the end of the code, else it will be a indefinite loop (2) initiating the counter 
42 | List comprehensions | works only for `for` loops...NOT with the `while` loop..can use `if` conditionals after for: `list = [<do_this> for <this> if <this>]`, after it is run, it returns the list as well
43 | Strings | Strings are tuples and behave like them - can be reference using index, can be looped....can be used with single or double quotes...if you are using one of the 2 in the string, use the other to encapsulate the string. >>> `print("Canada's capital is Ottawa")` >>> `print('He said "I am excited !"')` . 
44 | The escape character `\` | >>> `print('He said \"Canada\'s capital is Ottawa\"')`
45 | Escape characher usage | `\' `single quote. `\"` double quote, `\\` backslash, `\n` newline
46 | \n newline | added by default in print statement, can be changed >>> `print(<example>, end=' ')` - this will leave just one whitespace at the end of the <example> unlike the default newline
47 | triple quotes | `'''...'''` or  `""" ... """  ` ... allows to write a string of any length without worrying about lines
48 | String act as tuples | They can be indexed `'Example'[0]`, sliced `'Example'[:3]`, checked for length `len('Example')`, looped over like a tuple `for alphabet in 'Example':`, can be used for list comprehension `[alphabet for alphabet in 'Example']`...like tuples (and unlike lists) they are immutable, PROOF `'Example' == ('Example')`
49 | String methods | Change to all upper case >>>`'Example'.upper()` | Change to all lowercase`'Example.lower()`| check the length >>> `len('Example')` , | checking the index of the first occurance of a character >>>`'Example'.index('m')` also check the 1st occurance of a string`'Example'.index('mple')` | check if the string starts with something `'Example'.startswith('Exa')` | check if the string ends with something `'Example'.endswith('Exa')`
50 | Going between strings and lists: .split() and .join() | ***Split()*** is used to split a string into a list, the default point of splittin is a whitespace, other points can be specified - it returns a list of strings (which can be assigned to variables) >>>`e1, e2, e3 = 'Example is here'.split()` or `mm, dd, yy = '1/10/2021'.split('/')`. ***Join()*** is used to join a list of strings into a string, the splitting point has to be mentioned
51 | concatenate strings using + | you can add multiple strings into 1 string using >>> `Test1 = 'Example' + ' 23232'`. NOTE - any non string object has to be changed to a string using `str()` 
52 | f'string {} ..... ' | can be used to create/ print a string with a varible
53 | **Dictionaries** | starts and ends in {}, keys and values....and items (key/value pair) ... help(dict)
54 | accessing values using a key | creating dict `dict1 = {'key1':1,'key2':2, 'key3':3, 'key4':4, 'key5':5}`   , accesssing a value using key `dict1['key3']`, changing value using key >>> `dict1['key4'] = 44`
55 | Dictionary comprehension | similar to list comprehension, >>> `new_dict = {f'key{i+1}':f'value{i+1}' for i in [i for i in range(20)]}`
56 | using `in` to check for a key in a dict | `<key> in <dictionary>`, this will return True or False
57 | for loop in dictionaries | will loop over all its keys, >>> `for i in <dict>: print(i)`, looping over all values >>> `for i in <dict>: print(dict[i]) `, looping over all keys/values pairs >>> `for i,j in <dict>.items:` (i will be the key and j will be the value)():
58 | returning all keys and values of the dictionary | `<dictionary>.keys() `and `<dictionary>.values()`
59 | removing an iem | `<dictionary>.pop(<key>)`
60 | ***Working w/ external libraries*** | way to access them >>> `import pandas`, get help on the libraries: >>> `help(pandas)` , checking all the directories >>> `dir(pandas)`,type >>> `type(dir)`
61 | shorten form of an external library | >>> `import pandas as pd`, >>> `import numpy as np` >>> `import tensorflor as tf`
62 | Calling variables in a library by it name only | this CAN make life easier >>> `from math import *` >>> `pi` >>> `3.141592653589793`  (this is easier than writing >>> `math.pi` >>> `3.141592653589793`) ... this can ALSO cause bugs which are difficult to detect and fix (especially if you are calling all variables from multiple libraries and they have the same function doing different things), solution (1) call only the methods that you want from a library >>> `from math import log, pi` >>> `from numpy import asarray` (2) use full forms, this will make the code easier to understand and debug
63 | accessing submodules | to be accessed by multiple dots, eg. >>> `numpy.random.randint()`
64 | While working with external libraries, the 3 most important functions in Python | >>> `type()` >>> `dir() `>>> `help()`
65 | Operator overloading | Each library can define its own working with objects. When we do `dir(pandas)`, the methods that have 2 underscores at the start and at the end, e.g. `__getattr__`  are related to operator overloading.
66 | **Kaggle Course - 2/18** | **Pandas - https://www.kaggle.com/learn/pandas**
67 | Pandas | the most polular Python library for Data Analysis
68 | Importing Pandas | `import pandas as pd`
69 | Creating Data | Two core objects in Pandas - the **DataFrame** and the **Series**
70 | ***Series*** | A sequence of data values or a list >>> `<Series1> = pd.Series(<list>)`
70a | Optional index and Series name | `Series1 = pd.Series(<list>, index = [...], name ='list_name`)...the series name can act as the column if the series is used to create a df
71 | DataFrame | it is a Table, contains a 2x2 array of individual entries, each has a certain value. Each enty corresponds to a row (or a record) and a column...***input is mostly a dictionar***y >>> `dict = {'Name':['GSP', 2 ,'DSP'], 'Favorite Color':['Red', 0 ,'Blue']}` >>> `df = pd.DataFrame(<dict>) `
71a | Optional index | >>> `pd.DataFrame(<dict>, index = ['index1','index2',...]) `
71b | naming the default index column | `df.index.name = '<index_name>'`
71c | checking the shape of a df | `df.shape`
72 | **Sample dataset** | https://www.kaggle.com/carlolepelaars/toy-dataset
72 | reading a CSV file into a df | `pd.read_csv('file path')`
72a | reading a CSV and using one of its columns as index | >>> `pd.read_csv('file path', index_col=0)`...this is not a very good way as one could end up using a column that has duplicate values(s), thus the index will not be unique
73 | reading a CSV file in a ZIP file into a df | https://github.com/Govind-Patwal/European_Hotel_Analysis/blob/main/Data_Preprocessing/Step1_Deleting_Null_Values_and_dividing_into_2_tables.ipynb
74 | checking the shape of a df | `df.shape`
75 | checking the first and last 10 rows | >>>`df.head()` >>> `df.tail()`
76 | choosing a column from the CSV as the index | `pd.read_csv('file path', index_col=<column_number>)`
77 | saving to a CSV file | `<df>.to_csv('<file_path>)`
77a| w/o the index | `<df>.to_csv('<file_path>, index = False)`
78 | ***Accessing Data*** | 
78a | Accessing using Columns | >>>`df['column_name']`, accessing a value (column -> row)  >>>`df['column_name'][<row_index>]`....or first 10 rows of a column >>> `df['column_name'][:10]`
 78b | ***Accessing using Rows index first, followed by column index...iloc*** | >>>`df.iloc[<row_index_number>]` >>> `df.iloc[<row_index_number>,<column_index_number>]`...first 10 rows of a column and 4 columns >>> `df.iloc[:10, :4]`....can also pass any type of list for indexing >>> `df.iloc[[2,4,5,67,8,10],[2,3,4,5]]`...can also be used like >>> `df['column_label'].iloc[0]`
 79 | ***Accessing using Rows index first, followed by column label(s)...loc*** | >>>`df.loc[<row_index_number>, 'column_name']` ...once can also pass a list of column names >>> `df.loc[:, ['column1_name', 'column2_name', 'column3_name']`...can also be used like >>> `df['column_label'].loc[0]`
 80 | choosing between iloc and loc | since iloc is purely index based, 0:10 will return 10 values (0,1....9)....on the other hand loc is label based so both the start and end points are included, so 0:10 will return 11 values (0,1,2...11)...it is specifically good for situations when you want all values returned according to label names...eg df.loc[:,'GradeA':'GradeD']
 81 | naming the default index column that has no name | `df.index.name = '<index_name>'`
 82 | Removing the default index and replacing with a column in the df (the values in column should be unique) | >>> `df.set_index('<column_name_with_unique_values_in_rows>')`
 83 | Conditional selection | >>> `df['column_label'] == 'Str'/num` ...this produces a series of True/False, which can be used inside a `loc` to select the relevant data
 84 | Using loc for selecting data based on conditional | >>> `df.loc[df['Column_label'] <conditinal operation>]`
 85 | using and and or | use the signs `&` and `|`
 86 | Pandas built in conditional selector - 1/3 | .isin([Value1, Value2, Value3,...]) , it checks if a value is in the list given, for example >>> `df.loc[df['City'].isin(['New Delhi', 'Bangkok', 'Toronto'])]`, it is short form of writing >>> `df.loc[df['City'] == 'New Delhi' | df['City'] == 'Bangkok' | df['City'] == 'Toronto']`
 87 | Pandas built in conditional selector - 2/3 | .between(Value1,Value2)...it checks if a value is between the given range (as in loc, both end points are included), for example >>> `df.loc[df['Salary'].between(50000,80000)]`
 87 | isnull() and isnotnull() | to check if the value in a column is null or not, for example >> `df['Salary'].notnull()`
 88 | Assigning data to column(s) | `df['Cities'] = 'New City'` or `df['Salary of Employee'] = 50000`
89 | Assigning data based on conditions | `df.loc[df['column_label'] <conditional expression>, 'column_name'] = value`, for example >>> `df.loc[df['Income'].between(40367.0,93669.0), 'Income'] = 50000`
90 | setting the max number of rows to be displayes in a jupyter notebook | >>> `pd.set_option("display.max_rows", 5)`
91 | **Summary function and maps** | involves operations that we can apply to the data to get the 'desired input'
92 | some summary functions | >>>`df['column label'].describe()` >>>`df['column label'].mean()` >>>`df['column label'].avg()` >>>`df['column label'].min() `>>>`df['column label'].max()` >>>`df['column label'].median()` >>>`df['column label'].count() `>>>`df['column label'].unique()`....to find the name and frequency of unique values >>> `df['column_name'].value_counts()`, returning of the index of the max value in a column >>> `df['column_name'].idxmax()`
93 | Pandas (operations to create new columns in a jiffy)  | >>> `df['<new_column>'] = df['<column_1>'] + df['<column_2>']` + ' ' ...all mathimatical operations can be done, some more examples >>> `df['<new_column>'] = df['<column_1>'] - df['<column_1>'].mean()
94 | [Maps and apply](https://www.kaggle.com/residentmario/summary-functions-and-maps) - ways to to more advanced things likes applying conditional logic, anything needing a function | extremely useful for transforming data into new one...map() used for a single column /Series >>> `df['column label'].map()`...apply() used for entire dataframes >>> `df.apply(, axis='columns' OR 'index')` ... axis = 'columns' means the function will transform each row (with the column as the axis), axis = 'index' means the funtion will transform each column (with the index/rows as the axis)
95 | [**Grouping and Sorting**](https://www.kaggle.com/residentmario/grouping-and-sorting) | using groupby()
96 | Groupwise analysis | df.groupby('column_label')













---
## Job_search_keywords (for best result - use in combination)
- Very Good article - ***https://www.kdnuggets.com/2018/01/feizpour-becoming-data-scientist.html***

intern, internship
data analytics, data engineer
python engineer, python programmer

Google.com
Indeed
LinkedIn
Glassdooor

## Good_Links

### Links to Courses / Credits
- https://www.kaggle.com/learn/overview
- https://www.kaggle.com/learn/python 

### Links to profiles
- https://bluink.ca/
- https://bierman.io/
- https://github.com/BiermanM/job_scraper
- https://brittanyfortner.com/ 

- Stackoverflow

- https://aws.amazon.com/developer/language/python/?nc1=f_dr

- https://medium.com/@sjacks/using-rds-on-aws-with-jupyter-notebooks-c2703299fcc8
- https://towardsdatascience.com/amazon-rds-step-by-step-guide-14f9f3087d28
- https://amazon-rds.totableau.com/
- https://www.youtube.com/watch?v=PHsApsvZKNI
- some good GitHub page website - https://github.com/collections/github-pages-examples
- govind.github.io
- netflix.github.io
- https://github.com/Netflix/netflix.github.com

- http://twitter.github.io
- http://twitter.github.io/labella.js/

- Word to HTML converter - https://wordtohtml.net/
- Screen Capture (on Windows Appstore) - https://getsharex.com/
- Tech Interview Practice - https://leetcode.com/
- Kaggle



- https://www.youtube.com/watch?v=F5mRW0jo-U4




- Python on AWS - Mount the EFS to your Lambda function, intall dependencies on the EFS - https://www.youtube.com/watch?v=4cquiuAQBco
- Group Project - ML model on AWS - https://github.com/asadca4u/Final_Project_Group_Five 
- Group Project - Good Tableau - https://public.tableau.com/profile/kassie.lu#!/vizhome/AmesHousingSalesPricesDashboard/Dashboard?publish=yes
---

## Project_Ideas

***Banking*** - some very useful projects that are good for the resume and portfolio:
- Credit Fraud Detection: https://www.kaggle.com/mlg-ulb/creditcardfraud
- Customer Segmentation: https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python
- Two Sigma Financial Modeling: https://www.kaggle.com/c/two-sigma-financial-modeling
- The Winton Stock Market Challenge: https://www.kaggle.com/c/the-winton-stock-market-challenge
- New York Stock Exchange: https://www.kaggle.com/dgawlik/nyse
- Lending Club Loan Data: https://www.kaggle.com/wendykan/lending-club-loan-data
- Financial Machine Learning and Data Science: https://github.com/firmai/financial-machine-learning
- https://www.kaggle.com/arjunjoshua/predicting-fraud-in-financial-payment-services

---
Misc
- https://cloud.google.com/blog/topics/training-certifications/kick-off-2021-with-skill-badges-and-free-training


- https://towardsdatascience.com/6-data-science-certificates-to-level-up-your-career-275daed7e5df 


---