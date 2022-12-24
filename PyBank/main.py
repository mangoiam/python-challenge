#modules to import and read across path ways and read csv's

import os
import csv

#path to collect csv data
csvpath = os.path.join("Resources", "budget_data.csv")

month = []
profit_loss = []
profit_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next (csvreader)

    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

total_months = len(month)
net_profit = sum(profit_loss)

for i in range(1, len(profit_loss)):
    profit_change.append(profit_loss[i] - profit_loss[i-1])

Average_change = sum (profit_change) / len(profit_change)
    
max = profit_change.index(max(profit_change))
max_increase = (f"{month[max +  1]} (${profit_change[max]})")

min = profit_change.index(min(profit_change))
min_decrease = (f"{month[min +  1]} (${profit_change[min]})")

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profits: {max_increase}")
print(f"Greatest Decrease in Profits: {min_decrease}")

with open ('./analysis.txt' , 'w') as file:

    file.write("Financial Analysis\n")
    file.write("--------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: ${Average_change}\n")
    file.write(f"Greatest Increase in Profits: {max_increase}\n")
    file.write(f"Greatest Decrease in Profits: {min_decrease}\n")
    file.close()