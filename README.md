# **Unit 2 | Homework Assignment: Automate Your Day Job with Python**
---
## **PyBank**

### **Objective**
To analyze the financial records of a company and calculate the following
1.  The total number of months included in the dataset
2.  The net total amount of Profit/Losses over the entire period
3. The average of the changes in Profit/Losses over the entire period.
4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in losses (date and amount) over the entire period.

### **Data**
The data set is stored in the [Budget.csv](PyBank/Data/budget_data.csv) file and has two columns : Date and Profit/Losses

### **Technology**
*  Python 


[Main-prgram](/PyBank/main.ipynb)
```Python
#PyBank
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
print(f"Total Number of Months: {no_of_months}")
print(f"Total Profit/Loss: ${total_pnl}")
print(f"Average Change: ${round(total_change/no_change_month,2)}")
print(f"Greatest increase in Profits: {greatest_increase_month} (${greatest_increase_profit})")
print(f"Greatest decrease in Proftis: {greatest_decrease_month} (${greatest_decrease_profit})")

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

```

### **Output**

[Output text file ](/PyBank/output.txt)


---
---

## **PyRamen**

### **Objective**
Ichiban Ramen has closed it second year of the sales. To analyze how well  business did on a per-product basis.

### **Data**

The data is stored in csv files - [Menu_data.csv](PyRamen/Data/menu_data.csv) and [Sales_data.csv](Pyramen/Data/sales_data.csv)

## **Technology**
*  Python 

[Main-prgram](/PyRamen/main2.ipynb)

```Python
#PyRamen
#import the csv and path lib
import csv 
from pathlib import Path

#storing the file paths
menu_filepath=Path("Data/menu_data.csv")
sales_filepath=Path("Data/sales_data.csv")

#Initializing dictionaries to store the menu data and sales datea
menu=[]
sales=[]

#Reading menu data csv file to menu dictionary
with open(menu_filepath) as menu_file:
    reader2 = csv.reader(menu_file)
    next(reader2)
    for row in reader2:
        menu.append({'items':row[0],'category':row[1],'description':row[2],'price':row[3],'cost':row[4]})

#Reading sales data csv file to sales dictionary
with open(sales_filepath) as sales_file:
    reader2 = csv.reader(sales_file)
    next(reader2)
    for row in reader2:
        next(reader2,None)
        #print(row)
        sales.append({'Line_item_ID':row[0],'Date':row[1],'Credit_Card_Number':row[2],'Quantity':row[3],'Menu_Item':row[4]})

#Initialize an empty report dictionary to hold the future aggregated per-product results.
report={}
for sales_item in sales:
    menu_item=sales_item['Menu_Item']
    quantity=int(sales_item['Quantity'])
    if menu_item not in report:
        report[menu_item]={
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
            }

for sales_item in sales:
    sales_item_name=str(sales_item['Menu_Item'])
    for item in menu:
        if str(item['items'])==sales_item_name:
            quantity =int(sales_item['Quantity'])
            price=float(item['price'])
            cost=float(item['cost'])
            report[sales_item_name]["01-count"] += quantity
            report[sales_item_name]["02-revenue"] += price * quantity
            report[sales_item_name]["03-cogs"] += cost * quantity
            report[sales_item_name]["04-profit"] += (price-cost) * quantity

#printing the output        
print(report)

# Writing the results into the output2 text file
import sys
import os
import json


if os.path.exists("output2.txt"):
    os.remove("output2.txt")
output_file=open("output2.txt", "w") 
output_file.write(json.dumps(report))
output_file.close()
```

### **Output**

[Output text file ](/PyRamen/output2.txt)

---








