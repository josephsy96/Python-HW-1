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
vote_list = []
politics = []
ballot_num = {}
#==================================================
#reading the csv file
with open(pypoll, newline="") as outfile:
    header = next(outfile)
    poll_read = csv.reader(outfile, delimiter = ',')

#==================================================
    for row in poll_read:
        vote_list.append(row[0])
        politics.append(row[2])
#==================================================
#To create a dictionary for politicians' name and total votes
for name in politics:
    if name not in ballot_num:
        ballot_num[name] = 1
    else:
        ballot_num[name] += 1
#==================================================
#variables for total votes and winner totals
total_votes = len(vote_list)
winner_total = max(ballot_num.values())
#finding the winner
for winner in ballot_num:
    if ballot_num[winner] == winner_total:
        winner_name = winner
#==================================================
#Print output
print("Election Results")
print("---" * 10)
print(f"Total Votes: {total_votes}")
print("---" * 10)
#==================================================
#create an iterating output for candidates and votes
for key, value in ballot_num.items():
    print(f"{key}:  {round(((value/total_votes)* 100.00),3)}%  ({value})")
#==================================================

print("---" * 10)
print(f"Winner: {winner_name}")
print("---" * 10)
#==================================================
#output to txt file
with open("output.txt", 'w') as out:
    print("Election Results",file=out)
    print("---" * 10,file=out)
    print(f"Total Votes: {total_votes}", file=out)
    print("---" * 10, file=out)
#==================================================
    for key, value in ballot_num.items():
        print(f"{key}:  {round(((value/total_votes)* 100.00),3)}%  ({value})", file=out)
#==================================================
    print("---" * 10, file=out)
    print(f"Winner: {winner_name}", file = out)
    print("---" * 10, file = out)

