"""
Author: Joseph Yi
Date Created: October 26, 2019
"""
import csv
import os


#This is to set my current working directory
    #Change if you must. 
pull_folder = '/Users/josephyi/Python-HW-1/PyBank/Resources'
os.chdir(pull_folder)
#=============================================================
#This is to set 
pybank = os.path.join('../Resources', 'budget_data.csv')


#list created to compute later functions
net = []
date = []
with open(pybank, newline="") as bank_out:
    net_header = next(bank_out)
    bank_read = csv.reader(bank_out, delimiter = ',')
    #net_total = 0

    for csv_row in bank_read:
        net.append(csv_row[1])
        date.append(csv_row[0])
        net_total = sum(map(int, net))
        row_count = len(net)

    sub = int(net[-1]) - int(net[0])
    average_change = round(sub/(row_count - 1),2)
    max_profit = max(map(int,net))
    min_profit = min(map(int,net))
    month = 0
#output final product    
    print("Financial Analysis")
    print("---" * 10)
    print(f"Total Months: {row_count}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change:${average_change}")
    print(f"Greatest Increase in Profits: ${max_profit}")
    print(f"Greatest Decrease in Profits: ${min_profit}")
    print("---" * 10)
