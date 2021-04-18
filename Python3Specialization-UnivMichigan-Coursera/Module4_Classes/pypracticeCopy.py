'''
This Course is one of the main reason I joined this specialization.
It provides an intro to Classes and Inheretance.
'''

# import moudules

# define functions and classes

# define the main function that has the variables to be run for this program
def main ():
    print("n", '\t', "2**n")     #table column headings
    print("---", '\t', "-----")

    for x in range(13):        # generate values for columns
        print(x, '\t', 2 ** x)


# include a statement that makes sure that any file that imported this does not
# run the whole code

if __name__ == '__main__':
    main()


    