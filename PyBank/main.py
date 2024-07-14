import os
import csv


import csv


with open("Resources/budget_data.csv", mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
