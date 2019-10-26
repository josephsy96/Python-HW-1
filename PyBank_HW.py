"""
Author: Joseph Yi
Date Created: October 26, 2019
"""
import csv
import os


#This is to set my current working directory
    #Change if you must. 
pull_folder = '/Users/josephyi/Python-HW1/PyBank/Resources'
os.chdir(pull_folder)
#=============================================================
#This is to set 
pybank = os.path.join('../Resources', 'budget_data.csv')
def main():
    with open(pybank, newline="") as bank_out:
        net_header = next(bank_out)
        bank_read = csv.reader(bank_out, delimiter = ',')
        net_total = 0     
        average_change = 0.0
        row_count = sum(1 for row in bank_read)
#This section of code is to calculate the total net amount of the csv file.      
        for money_row in bank_read:
            net_total += int(money_row[1])
        for average in 


    print("Financial Analysis")
    print("---" * 10)
    print(f"Total Months: {bank_read.line_num}")
    print(f"Net Total: ${net_total}")
    #print(f"Average Change:{average_change}")
    print("---" * 10)

if __name__=="__main__":
    main()
