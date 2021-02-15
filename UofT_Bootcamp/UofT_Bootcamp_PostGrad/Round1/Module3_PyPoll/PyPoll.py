import csv

with open('Resources/election_results.csv') as data_file:
    print(data_file)
    voters_data = csv.reader(data_file)
    for row in voters_data: 
        print(row)    