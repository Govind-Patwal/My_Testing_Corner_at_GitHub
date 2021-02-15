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

    county_list = []
    votes_per_county = {}


    for row in file_reader:
        # calculation for total votes
        i += 1

        # calculation for candidates votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1

        # calculation for county votes
        if row[1] not in county_list:
            county_list.append(row[1])
            votes_per_county[row[1]] = 1
        else:
            votes_per_county[row[1]] += 1    


for candidate in votes_per_candidate:
    print(f'{candidate} got {votes_per_candidate[candidate]:,} votes and {votes_per_candidate[candidate]/i*100:.2f} % of votes.')

election_winner_candidate = max(votes_per_candidate, key=votes_per_candidate.get)   
election_winner_county = max(votes_per_county, key=votes_per_county.get) 


election_summary = (
    f'The total number of votes cast were: {i:,}\n'
    f'===============================================\n'
    f'===========Candidate summary =====================\n'
    f'===============================================\n'
    f'The candidate list is : {candidate_list}\n'
    f'===============================================\n'
    f'Vote count per candidate is {votes_per_candidate}\n'
    f'The candidate winner of the election was {election_winner_candidate} with {votes_per_candidate[election_winner_candidate]:,} votes\n'
    f'===============================================\n'
    f'===========County summary =====================\n'
    f'===============================================\n'
    f'The county list is : {county_list}\n'
    f'===============================================\n'
    f'Vote count per county is {votes_per_county}\n'
    f'The county winner of the election was {election_winner_county} with {votes_per_county[election_winner_county]:,} votes\n'
)

print(election_summary)

# saving the data
with open('my_summary.txt', 'w') as text_file: 
    text_file.write(election_summary)