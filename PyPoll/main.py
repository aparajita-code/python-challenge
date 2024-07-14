import csv
#reading the csv file
with open("Resources/election_data.csv", mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)