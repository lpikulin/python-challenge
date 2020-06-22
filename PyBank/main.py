#Linda Pikulin
#Python Challenge
#PyBank

import os
import csv


os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath=os.path.join((os.path.dirname(os.path.abspath(__file__))),"Resources","budget_data.csv")
print(csvpath)

date=[]
profit=[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    print(f"CSV Header:{csv_header}")
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))

#print(f"{date[0]} {profit[0]}")
months=len(date)
print("Financial Analysis")
print("-----------------")
print(f"Total months: {months}")
total=sum(profit)
formatted_total="${:,.2f}".format(total)
print(f"Total: {formatted_total}")
avg="${:,.2f}".format(total/months)
print(f"Average change: {avg}")
max="${:,.2f}".format(max(profit))
print(f"Greatest increase in profits: {max}")
min="${:,.2f}".format(min(profit))
print(f"Greatest decrease in profits: {min}")

file1=open(os.path.join((os.path.dirname(os.path.abspath(__file__))),"analysis","pybank_output.txt"),'a')
file1.write("Financial Analysis\n")
file1.write("-----------------\n")
file1.write("Total months: "+ str(months)+"\n")
file1.write("Total: "+str(formatted_total)+"\n")
file1.write("Average change: "+str(avg)+"\n" )
file1.write("Greatest increase in profits: "+str(max)+"\n")
file1.write("Greatest decrease in profits: "+str(min))
file1.close