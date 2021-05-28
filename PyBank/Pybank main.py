#import csv library
import csv as csv

#Initializing the dictionary Budget Data
Budget_Data={"Date":"Profit/Losses"}

#Reading csv file and loading it into dictionary
with open('Data/budget_data.csv') as budget_file:
    reader2 = csv.DictReader(budget_file)
    for row in reader2:
        Budget_Data[row['Date']]=row['Profit/Losses']

#Initialising Variables
no_of_months=0
total_pnl=0
current_pnl=0
previous_pnl=0
Change_pnl ={}
average_change=0
greatest_increase_profit=0
greatest_decrease_profit=0
greatest_increase_month=0
greatest_decrease_month=0
total_change=0
no_change_month=0


#calculating the change in Profit/Losses
for month, pnl in Budget_Data.items():
    if month !="Date":
        no_of_months=no_of_months+1
        total_pnl=total_pnl+int(pnl)
        if previous_pnl==0:
            previous_pnl=int(pnl)
            current_pnl==0
            Change_pnl[month]=0
        else :
            current_pnl=pnl
            Change_pnl[month]= int(current_pnl)-int(previous_pnl)
            previous_pnl=pnl

#calculating greatest increase and decrease in profits
for change_month,change_pnl in Change_pnl.items():
    if change_pnl !=0 :
        total_change=total_change+change_pnl
        no_change_month=no_change_month+1
    if greatest_increase_profit==0 and greatest_decrease_month==0:
        greatest_increase_profit=change_pnl
        greatest_decrease_profit=change_pnl
    elif change_pnl > greatest_increase_profit:
        greatest_increase_profit=change_pnl
        greatest_increase_month=change_month
    elif change_pnl < greatest_decrease_profit:
        greatest_decrease_profit=change_pnl
        greatest_decrease_month=change_month

#Displaying output ot the terminal
print("\tFinancial Analysis")
print("-"*100)
print("Total Number of Months: "+str(no_of_months))
print("Total Profit/Loss: $"+str(total_pnl))
print("Average Change: $"+str(round(total_change/no_change_month,2)))
print("Greatest increase in Profits: "+ str(greatest_increase_month)+" ($"+str(greatest_increase_profit)+")")
print("Greatest decrease in Proftis: "+str(greatest_decrease_month) +" ($"+str(greatest_decrease_profit)+")")

import sys
import os

#Writing output to text file
if os.path.exists("output.txt"):
    os.remove("output.txt")
output_file =open("output.txt", "w")
output_file.write("\t"+"Financial Analysis -ASHWEEJ"+"\n")
output_file.write("--------------------------------------------"+"\n")
output_file.write("Total Number of Months: "+ str(no_of_months) + "\n")
output_file.write("Total Profit/Loss: $"+ str(total_pnl)+"\n")
output_file.write("Average Change: $"+ str(round(total_change/no_change_month,2))+"\n")
output_file.write("Greatest increase in Profits: "+ str(greatest_increase_month)+" ($"+ str(greatest_increase_profit)+")"+"\n")
output_file.write("Greatest decrease in Proftis: "+ str(greatest_decrease_month)+" ($"+ str(greatest_decrease_profit)+")"+"\n")
output_file.close()