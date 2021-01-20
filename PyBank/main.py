import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

months = []
net_total = []



with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    header = next(csvreader)


    for row in csvreader:
        print(row)

        months.append(row[0])
        net_total.append(int(row[1]))


total_months = len(months)

total_change = sum(net_total)




Total_average = []
Total_average = sum(total_change) / len(total_change)

for i in range(len(net_total)-1):
    total_average.append(net_total[i+1]-net_total[i])




greatest_increase = max(total_change)
greatest_decrease = min(total_change)


     
            

print('Financial Analysis')
print('-----------------------------')
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(sum(total_change)))
print("Average Change: " + "$" + str(total_average))
print("Greatest Increase in Profits: " + "$" + str(months[total_change.index(max(total_change))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + "$" + str(months[total_change.index(max(total_change))+1]) + " " + "$" + str(greatest_decrease))



