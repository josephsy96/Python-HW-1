"""
Author: Joseph Yi
Created: October 30, 2019
"""
import os
import csv
#==================================================
#Setting current directory
pull_folder = '/Users/josephyi/Python-HW-1/PyPoll/Resources'
os.chdir(pull_folder)
#delete above if need to. 
pypoll = os.path.join('../Resources', 'election_data.csv')
#==================================================
#creating lists
vote = []
politics = []
#==================================================
#reading the csv file
with open(pypoll, newline="") as outfile:
    header = next(outfile)
    poll_read = csv.reader(outfile, delimiter = ',')

#==================================================
    for row in poll_read:
        vote.append(row[0])
        politics.append(row[2])
for vote_index in range(len(politics)):
    voting = str(politics[vote_index])
    election = str(vote[vote_index])


total_votes = len(vote)

print("Election Results")
print("---" * 10)
print(f"Total Votes: {total_votes}")
print("---" * 10)
print(f"{election} {voting}")



