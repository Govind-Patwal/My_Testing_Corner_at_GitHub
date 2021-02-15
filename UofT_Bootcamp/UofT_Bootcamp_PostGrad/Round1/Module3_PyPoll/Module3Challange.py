# import dependencies
import csv

#reading in the file
with open('Resources/election_results.csv') as election_data:
    data_for_file = csv.reader(election_data)

    headers = next(data_for_file)
    print(headers)

    voter_count = 0
    county = []
    county_votes = {}

    for rows in data_for_file:
        # counter for total number of votes
        voter_count += 1

        # declaring a variable for city
        x = rows[1]

        # creating a list of all county names
        if x not in county:
            county.append(x)
            county_votes[x] = 1
        else:
            county_votes[x] += 1  

print(voter_count)       
print(county)
print(county_votes)

#         Download the PyPoll_Challenge_starter_code.py file and rename it PyPoll_Challenge.py.
# Use the step-by-step instructions below to add code where indicated by the numbered comments in the starter code file.
        

# Step 1:

# Initialize a county list, like the candidate_options list, that will hold the names of the counties.
# Initialize a dictionary, like the candidate_votes dictionary, that will hold the county as the key and the votes cast for each county as the values.