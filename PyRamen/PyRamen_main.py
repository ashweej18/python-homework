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