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

Wk | DOW | Date | Planned | Executed | Evaluation
| --- | --- | --- | --- | --- | --- |
0 | Sun | 2020/12/13 | This Wk: Demo day + Relaxation | Bootcamp finished last Sunday (12/06). 1st 4 days of this week spent on Practicing for Demo day on 12/10; Sat/Sun spent relaxing | 
1 | Mon | 2020/12/14 | Planning for this Wk | Google's Python Class + laptop setup. New Laptop delivered on 12/14 |
1 | Tue | 2020/12/15 | Google's Python Class + laptop setup  | Setting up new Laptop, partitioning (created D: for non-OS)|
1 | Wed | 2020/12/16 | Google's Python Class + laptop setup  | Installing Git, Python, Anaconda - checking for opening .ipynb files from outside D:, copying files from oustside | 
1 | Thu | 2020/12/17 | Google's Python Class + laptop setup  | Copying files from outside, setup complete, started Google Python class | 
1 | Fri | 2020/12/18| Google's Python Class + laptop setup | Started Google Python Class, found it was Python 2, so dropped this plan - found more courses on pyhon.org, and W3 schools, but decided to go through UofT Bootcamp modules again |
1 | Sat | 2020/12/19 | Google's Python Class + laptop setup | Spent time on ways to create Video with Green backgound so that I could create educational videos and put on GitHub - tried Zoom, Logitech Capture, Logitech Gaming, OBS, Chroma Cam , Personify | 
1 | Sun | 2020/12/20| Google's Python Class + laptop setup | Started with Bootcamp Python, moved to working on Career Service tasks - finished the intro, now working on others parts, decided to use the next 2 Wks to complete all tasks related to becoming Employee Ready and Employee Competitive and then revisit Hard/Soft Skills| Plan changed mid-wk
2 | Mon | 2020/12/21| Planning for this Wk | Change of plans - to Exercise everyday, am willing to push the Job start date by 2-4 months to achieve this |
2 | Tue | 2020/12/22| Complete tasks to become Employer-Ready | WIP |
2 | Wed | 2020/12/23| Complete tasks to become Employer-Ready | WIP  |
2 | Thu | 2020/12/24| Complete tasks to become Employer-Ready | WIP  |
2 | Fri | 2020/12/25| Complete tasks to become Employer-Ready | WIP  |
2 | Sat | 2020/12/26| Complete tasks to become Employer-Ready | WIP  |
2 | Sun | 2020/12/27| Complete tasks to become Employer-Ready | Completed on time | 100% completed 
3 | Mon | 2020/12/28| Planning for this Wk | to complete portfolio- GitHub Pages |
3 | Tue | 2020/12/29| to complete portfolio- GitHub Pages |  |
3 | Wed | 2020/12/30| to complete portfolio- GitHub Pages |  |
3 | Thu | 2020/12/31| Relax |  |
3 | Fri | 2021/1/1| Relax |  |
3 | Sat | 2021/1/2| Relax |  |
3 | Sun | 2021/1/3| Start Python | working on Kaggle Python course - https://www.kaggle.com/govindpatwal/exercise-booleans-and-conditionals/edit |
---

### Cheat_Sheet

Number | Action | Shortcut
|---|---|---|
1 | Checking the version of Python in Windows | cmd -> type `python --version`
2 | Running a python file | cmd -> cd to the root where file is placed -> python <filename>
3 | Opening a .pynb file in D: | open Anaconda prompt -> d: -> jupyter notebook
3a | help in python | help()
3b | print in python | print(x), help(print), print(x, end =' ' )
4 | check the data type in python | type(23) / type ('String')
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
42 | List comprehensions | works only for `for` loops...NOT with the `while` loop..can use `if` conditionals after for: `list = [<do_this> for <this> if <this>]`
43 | Strings | Strings are tuples and behave like them - can be reference using index, can be looped....can be used with single or double quotes...if you are using one of the 2 in the string, use the other to encapsulate the string. >>> `print("Canada's capital is Ottawa")` >>> `print('He said "I am excited !"')` . **BEST: use the escape character `\` >>> `print('He said \"Canada\'s capital is Ottawa\"')`**








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