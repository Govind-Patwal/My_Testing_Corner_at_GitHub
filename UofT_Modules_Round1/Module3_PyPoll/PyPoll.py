#1 adding dependencies
import csv

# Initialize the total vote counter
total_votes = 0
candidate_list = []
candidate_vote = {}
# open the csv
with open('Resources/election_results.csv') as election_data:
    # read the csv
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    for rows in file_reader:
        #code to find the total vote count
        total_votes +=1

        # candidate name
        candidate = rows[2]

        # code to find all unique candidates
        if rows[2] not in candidate_list:
            candidate_list.append(candidate) 
            candidate_vote[candidate] = 1
        else:
            candidate_vote[candidate] += 1

        # else:
        #     candidate_vote[rows[2]] +=1     

print(candidate_list)
print(candidate_vote)
#2 the number of  candidates

#3 the number of votes received by each candidate

#4 the percentage of votes each candidate received

#5 the winner of the election
