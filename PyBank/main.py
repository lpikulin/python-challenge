#Linda Pikulin
#Python Challenge
#PyBank
#I have to cd of the terminal to the folder holding my data file for this to work


import pandas
df=pandas.read_csv('budget_data.csv',delimiter=",")
months=(df['Date'].count())
print("Financial Analysis")
print("-----------------")
print(f"Total months: {months}")
total=(df['Profit/Losses'].sum())
formatted_total="${:,.2f}".format(total)
print(f"Total: {formatted_total}")
avg="${:,.2f}".format(df['Profit/Losses'].mean())
print(f"Average change: {avg}")
max="${:,.2f}".format(df['Profit/Losses'].max())
print(f"Greatest increase in profits: {max}")
min="${:,.2f}".format(df['Profit/Losses'].min())
print(f"Greatest decrease in profits: {min}")
