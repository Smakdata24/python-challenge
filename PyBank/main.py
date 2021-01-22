import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

months = []
total_profit = []
monthly_profit_change = []



with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    header = next(csvreader)


    for row in csvreader:


        months.append(row[0])
        total_profit.append(int(row[1]))



    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])





greatest_increase = max(monthly_profit_change)
greatest_decrease = min(monthly_profit_change)



max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 






     
            

print('Financial Analysis')
print('-----------------------------')
print(f"Total Months: {len(months)}")
print(f"Total: + ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(greatest_decrease))})")






text_file = path("python-challenge", "PyBank", "Analysis.txt")

with open(text_file, "W") as file



file.write("Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: + ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(greatest_decrease))})")



















