import os 
import csv
from statistics import mean

budget_csv = os.path.join(r'C:\Users\kylem\Desktop\Bootcamp_Assignments\python-challenge\PyBank\Resources\budget_data.csv')
output_text = os.path.join(r'C:\Users\kylem\Desktop\Bootcamp_Assignments\python-challenge\PyBank\analysis\pybank.txt')

#Opens and reads budget_data.csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    
    #sets "months" and "net" to 0 to count in the loop.
    #Created lists for profit, months and change in profit as I will be using these lists in determining the greatest increase, decrease and the months associated with those changes
    
    month = 0
    net = 0
    profit = []
    change = []
    month_list = []

    for row in csvreader:

        #adding all the rows except the header row to show total months
        month += 1

        # sum of the profit/loss column to provide net profit
        net += float(row[1])

        #creates a list of profits/losses. This list is later used to find the difference between profits per month
        profit.append(float(row[1]))
        
        #creates a list of months which is later used when determining which month had the largest increase and decrease in profits
        month_list.append(str(row[0]))
        

        #Loops throught the "profit" list, finds the difference between the values and adds each difference to a list named "change"
        # The index of the greatest change value in the "change" list is compared with the index of the "month_list" to retrieve the month associated with greatest increase and decrease of profits

    for i in range(1,len(profit)):
        change.append(profit[i] - profit [i-1])
        ave_change = round(sum(change) / len(change), 2)
        greatest_increase = max(change)
        location = change.index(greatest_increase)
        month_increase = month_list[int(location) +1]
        greatest_decrease = min(change)
        location_2 = change.index(greatest_decrease)
        month_decrease = month_list[int(location_2) +1]


f = open(output_text, 'a')
print("Financial Analysis", file=f)
print("----------------------", file=f)   
print ("Total Months: ",month, file=f)
print ("Total: $",net, file=f)
print ("Average Change: $",ave_change, file=f)
print ("Greatest Increase in Profits:", month_increase,"$", "(",greatest_increase,")", file=f)
print ("Greatest Decrease in Profits:", month_decrease, "$", "(",greatest_decrease,")", file=f)
f.close()





