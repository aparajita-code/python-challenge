

import csv

####################################################
# Initialize variables
total_months = 0
net_total = 0
previous_month = 0
changes = []

max_increase = float("-inf")
max_decrease = float("inf")
max_increase_date = ""
max_decrease_date = ""

# Reset the file pointer to the beginning of the file
with open('Resources/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        total_months += 1  #
        profit_loss = int(row[1])
        net_total += profit_loss



        if total_months == 1:
            previous_month = profit_loss
        else:
            change = profit_loss - previous_month
            changes.append(change)
            date = row[0]

            if change>max_increase :
                max_increase=change
                max_increase_date = date

            if change < max_decrease:

                max_decrease = change
                max_decrease_date = date
            previous_month = profit_loss


average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")

print("-----------------------------")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")


with open('Resources/bank_output.csv', 'w', newline='') as outfile:
    # vScode needs entire path of the file it seems
    # Write a single row
    outfile.write("Financial Analysis \n")
    outfile.write("------------------------\n")
    outfile.write(f"Total Months :{total_months}\n")
    outfile.write(f"Total: ${net_total}")
    outfile.write(f"Average Change :${average_change:.2f}\n")
    outfile.write("------------------------\n")
    outfile.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")




