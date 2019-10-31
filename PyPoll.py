"""
Author: Joseph Yi
Date Created: October 28, 2019
"""
import os
import csv

#========================================================
#This is to change my current working directory from the prior directory
    #Change if you must. 
#NOTE: if you need to comment out this section, do so!
pull_folder = '/Users/josephyi/Python-HW-1/PyPoll/Resources'
os.chdir(pull_folder)
#========================================================
#This is to set the path
pypoll = os.path.join('../Resources', 'election_data.csv')
#========================================================
#list created to compute data
vote = []
candidate = []
one_candidate = []
#========================================================
#This section is to read the csv file.
with open(pypoll, newline='') as py_out:
    py_header = next(py_out)
    pypoll_read = csv.reader(py_out, delimiter = ',')
#========================================================
#set the loop
    for row in pypoll_read:
       vote.append(row[0])
       candidate.append(row[2])
       total_votes = len(vote)
      
#========================================================
# look at house of pies activity in day 2          
 

    


print("Election Results")
print("---" * 10)
print(f"Total Votes: {total_votes}")

print("---" * 10)
print("Winner:")
print("---" * 10)






