"""
Author: Joseph Yi
Date Created: October 26, 2019
"""
import csv
import os

#========================================================
#This is to change my current working directory from the prior directory
    #Change if you must. 
#NOTE: if you need to comment out this section, do so!
pull_folder = '/Users/josephyi/Python-HW-1/PyBank/Resources'
os.chdir(pull_folder)
#========================================================
#This is to set the path
pybank = os.path.join('../Resources', 'budget_data.csv')

#========================================================
#list created to compute later functions
net = []
date = []

#========================================================

with open(pybank, newline='') as bank_out:
    net_header = next(bank_out)
    bank_read = csv.reader(bank_out, delimiter = ',')
    #net_total = 0
#========================================================
    for csv_row in bank_read:
        net.append(csv_row[1])
        date.append(csv_row[0])
        net_total = sum(map(int, net))
        row_count = len(net)
#========================================================
#calculate the range average
    sub = int(net[-1]) - int(net[0])
    average_change = round(sub/(row_count - 1),2)
    max_profit = max(map(int,net))
    min_profit = min(map(int,net))
#========================================================
#Combine my net list and date list into a dictionary
    dictionary = dict(zip(net,date))
    max_month = dictionary[str(max_profit)]
    min_month = dictionary[str(min_profit)]
#========================================================
    #output final product 
    print("Financial Analysis")
    print("---" * 10)
    print(f"Total Months: {row_count}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change:${average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")
    print("---" * 10)
#========================================================
# This section outputs the print statements into a text file.
    with open("output.txt", 'a') as out:   
        print("Financial Analysis", file=out)
        print("---" * 10,file=out)
        print(f"Total Months: {row_count}",file=out)
        print(f"Net Total: ${net_total}", file=out)
        print(f"Average Change:${average_change}",file=out)
        print(f"Greatest Increase in Profits: {max_month} (${max_profit})",file=out)
        print(f"Greatest Decrease in Profits: {min_month} (${min_profit})",file=out)
        print("---" * 10,file=out)
    
#========================================================


