#1 adding dependencies
import csv

# open the csv
with open('Resources/election_results.csv') as election_data:
    # read the csv
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    for 

#2 the number of candidates

#3 the number of votes received by each candidate

#4 the percentage of votes each candidate received

#5 the winner of the election
