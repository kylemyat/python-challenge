import os 
import csv
from statistics import mean

budget_csv = os.path.join(r'C:\Users\kylem\Desktop\Bootcamp_Assignments\python-challenge\PyBank\Resources\budget_data.csv')


#Opens and reads budget_data.csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    
    #Total Months
    month = 0
    net = 0
    profit = []
    change = []
    previous_profit = 0
    month_list = []

    for row in csvreader:

        #adding all the rows
        month += 1

        # sum of the profit/loss column to provide net
        net += float(row[1])

        #creates a list of profits/losses 
        profit.append(float(row[1]))
        month_list.append(str(row[0]))
        

        #Loops throught the "profit" list, finds the difference between the values and returns the average
        
    for i in range(1,len(profit)):
        change.append(profit[i] - profit [i-1])
        ave_change = round(sum(change) / len(change), 2)
        greatest_increase = max(change)
        location = change.index(greatest_increase)
        month_increase = month_list[int(location) +1]
        greatest_decrease = min(change)
        location_2 = change.index(greatest_decrease)
        month_decrease = month_list[int(location_2) +1]

    
    
print ("Total Months: ",month)
print ("Total: $",net)
print ("Average Change: $",ave_change)
print ("Greatest Increase in Profits:", month_increase,"$", greatest_increase)
print ("Greatest Decrease in Profits:", month_decrease, "$", greatest_decrease)



