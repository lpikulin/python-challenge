#Linda Pikulin
#Python Challenge
#PyPoll
#I have to cd of the terminal to the folder holding my data file for this to work


import os
import csv


os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath=os.path.join((os.path.dirname(os.path.abspath(__file__))),"Resources","election_data.csv")
print(csvpath)

voterID=[]
county=[]
candidate=[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
 #   print(f"CSV Header:{csv_header}")
    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

voters=len(voterID)

print("Election Results")
print("-----------------")
print(f"Total voters: {voters}")
print("-----------------")
khan=0
correy=0
li=0
o=0

for x in range(0,voters):
     if candidate[x]=="Khan":
         khan=khan+1
     elif candidate[x]=="Correy":
         correy=correy+1
     elif candidate[x]=="Li":
         li=li+1
     elif candidate[x]=="O'Tooley":
         o=o+1

khan_pct="{:.3%}".format(khan/voters)
print(f"Khan:  {khan_pct} ({khan})")
correy_pct="{:.3%}".format(correy/voters)
print(f"Correy:  {correy_pct} ({correy})")
li_pct="{:.3%}".format(li/voters)
print(f"Li:  {li_pct} ({li})")
o_pct="{:.3%}".format(o/voters)
print(f"O'Tooley:  {o_pct} ({o})")
print("-----------------")

names=["Khan","Correy","Li","O'Tooley"]
totals=[khan,correy,li,o]

winner=totals.index(max(totals))
print(f"Winner: {names[winner]}")

file1=open(os.path.join((os.path.dirname(os.path.abspath(__file__))),"analysis","PyPoll.txt"),'a')
file1.write("Election Results\n")
file1.write("-----------------\n")
file1.write("Total voters: "+ str(voters)+"\n")
file1.write("-----------------\n")
file1.write("Khan: "+str(khan_pct)+" ("+str(khan)+")\n")
file1.write("Correy: "+str(correy_pct)+" ("+str(correy)+")\n")
file1.write("Li: "+str(li_pct)+" ("+str(li)+")\n")
file1.write("O'Tooley: "+str(o_pct)+" ("+str(o)+")\n")
file1.write("-----------------\n")
file1.write("Winner: "+ names[winner] +"\n")
file1.write("-----------------\n")
file1.close