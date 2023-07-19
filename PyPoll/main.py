import os
import csv


election_csv = os.path.join(r'C:\Users\kylem\Desktop\Bootcamp_Assignments\python-challenge\PyPoll\Resources\election_data.csv')
output_text = os.path.join(r'C:\Users\kylem\Desktop\Bootcamp_Assignments\python-challenge\PyPoll\analysis\pypoll.txt')

#opens and reads election_data.csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    #List of unique candidate names to determine the number of candidates running
    candidates = []

    #List of candidate names as seen in the CSV fiie. This list is used to determine the votes each candidate received based on the number of times the name appears in the list.
    all_candidates = []
    vote_1 = 0
    vote_2 = 0
    vote_3 = 0
    
    
    #Total number of votes set to 0 to add later
    votes = 0
    
    for row in csvreader:

        #adding all the rows to tally the total number of votes
        votes += 1

        #creating a new list of only candidate names. Each time the name appears in the list will be used to determine the number of votes for each candidate
        all_candidates.append(str(row[2]))
        
        
        #If statement to loop through the rows of the CSV to determine unique candidate names which determines the number of candidates
        if row[2] not in candidates:
            candidates.append(row[2])

    #Each candidate is held in their own variable based on the index in "candidates" list
    candidate_1 = candidates[0]
    candidate_2 = candidates[1]
    candidate_3 = candidates[2]
    running = len(candidates)

    
    #For loop of the "all_candidates" list to count the numbers of votes each candidate received
    for x in all_candidates:
        if x == candidate_1:
            vote_1 = vote_1 + 1
        if x == candidate_2:
            vote_2 = vote_2 + 1
        if x == candidate_3:
            vote_3 = vote_3 + 1
#To determine the Winner of the election, the IF statement will compare the number of votes each candidate received
win = max(vote_1, vote_2, vote_3)
if win == vote_1:
    winner = candidate_1
if win == vote_2:
    winner = candidate_2
if win == vote_3:
    winner = candidate_3

#Used a new variable to hold the percentage of votes each candidate received
vote_1p = round((vote_1 / votes * 100),3)
vote_2p = round((vote_2 / votes * 100),3)
vote_3p = round((vote_3 / votes * 100),3)

f = open(output_text, 'a')    
print("Election Results", file=f)
print("--------------------", file=f)
print("Total Votes: ", votes, file=f)
print("--------------------", file=f)
print(candidate_1,":", vote_1p, "%", " (",vote_1,") ", file=f)
print(candidate_2,":", vote_2p, "%", " (",vote_2,") ", file=f)
print(candidate_3,":", vote_3p, "%", " (",vote_3,") ", file=f)
print("--------------------", file=f)
print("Winner: ", winner, file=f)
f.close()