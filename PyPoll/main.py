import csv

from collections import Counter

#reading the csv file
with open('Resources/election_data.csv', 'r') as csvfile:
    # Reading the CSV file Done
    csvreader = csv.reader(csvfile)
    next(csvreader)
    candidates = [row[2] for row in csvreader]
    #Count occurrences of each value in the second column
    counts = Counter(candidates)
    total_rows = len(candidates)
    winner = max(counts, key=counts.get)
    # Print the summary
    for value, count in counts.items():
        percentage = (count / total_rows) * 100
        print(f'{value}: {count} : {percentage}')


    print(f"Winner : {winner}")

    print("Election Results")
    print("------------------------")
    print(f"Total number of votes:{total_rows}")













