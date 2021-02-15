import csv

# loading the file
with open('Resources/election_results.csv') as data_file:
    # opening the file
    file_reader = csv.reader(data_file)

    # read and skip the header row
    headers = next(file_reader)
    print(f'The headers of the data were {headers}')
    print('===============================================')

    i =0
    candidate_list = []
    votes_per_candidate = {}
    for row in file_reader:
        i += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1




print(f'The total number of votes cast were: {i:,}') 
print('===============================================')
print(f'The candidate list is : {candidate_list}')
print('===============================================')
print(f'Vote count per candidate is {votes_per_candidate}')
for candidate in votes_per_candidate:
    print(f'{candidate} got {votes_per_candidate[candidate]:,} votes and {votes_per_candidate[candidate]/i*100:.2f} % of votes.')

election_winner = max(votes_per_candidate, key=votes_per_candidate.get)   
print('===============================================')



election_summary = (
    f'The winner of the election was {election_winner} with {votes_per_candidate[election_winner]:,} votes \n'  
    f'The winner of the election was {election_winner} with {votes_per_candidate[election_winner]:,} votes' 
)  

with open('election_summary.txt', 'w') as text_file:
    text_file.write(election_summary)
