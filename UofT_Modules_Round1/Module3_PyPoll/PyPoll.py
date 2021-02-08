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


for candidate, votes in candidate_vote.items():
    print(f"{candidate}: {votes/total_votes*100:.1f} ({votes:,})\n")


# displaying the winning candidate and the % votes
# creating empty variable
winning_votes = 0
winning_candidate = ''
winning_percentage = 0

for candidate, votes in candidate_vote.items():
    if votes > 0 and votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes

winning_candidate_summary = (
    f"-------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Votes: {winning_votes:,}\n"
    f"Percentage: {winning_votes/total_votes*100:.2f}%\n"
    f"-------------------------------------------"
)
print(winning_candidate_summary)

with open('election_result2.txt', 'w') as text_file:
    text_file.write(winning_candidate_summary)