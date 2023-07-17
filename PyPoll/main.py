import os
import csv


election_csv = os.path.join(r'C:\Users\kylem\Desktop\Bootcamp_Assignments\python-challenge\PyPoll\Resources\election_data.csv')


#opens and reads election_data.csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    candidates = []
    all_candidates = []
    vote_1 = 0
    vote_2 = 0
    vote_3 = 0
    
    
    #Total number of votes
    votes = 0
    
    for row in csvreader:

        #adding all the rows
        votes += 1
        all_candidates.append(str(row[2]))
        
        

        if row[2] not in candidates:
            candidates.append(row[2])
           
    candidate_1 = candidates[0]
    candidate_2 = candidates[1]
    candidate_3 = candidates[2]
    running = len(candidates)

    
    
    for x in all_candidates:
        if x == candidate_1:
            vote_1 = vote_1 + 1
        if x == candidate_2:
            vote_2 = vote_2 + 1
        if x == candidate_3:
            vote_3 = vote_3 + 1

win = max(vote_1, vote_2, vote_3)
if win == vote_1:
    winner = candidate_1
if win == vote_2:
    winner = candidate_2
if win == vote_3:
    winner = candidate_3

vote_1p = round((vote_1 / votes * 100),3)
vote_2p = round((vote_2 / votes * 100),3)
vote_3p = round((vote_3 / votes * 100),3)

    
print("Election Results")
print("--------------------")
print("Total Votes: ", votes)
print("--------------------")
print(candidate_1,":", vote_1p, "%", " (",vote_1,") ")
print(candidate_2,":", vote_2p, "%", " (",vote_2,") ")
print(candidate_3,":", vote_3p, "%", " (",vote_3,") ")
print("--------------------")
print("Winner: ", winner)