import csv


from collections import Counter

#reading the csv file
# If running in Vscode then looks like the file location needs to be PyBank/Resources/election_data.csv

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

        print(f'{value}: {count} : {percentage:.2f}%')


    print(f"Winner : {winner}")

    print("Election Results")
    print("------------------------")
    print(f"Total number of votes:{total_rows}")

    with open('Resources/poll_output.csv', 'w', newline='') as outfile:
    # vScode needs entire path of the file it seems
    # Write a single row
        outfile.write("Election Results \n")
        outfile.write("------------------------\n")
        outfile.write(f"Total number of votes:{total_rows}\n")
        outfile.write("------------------------\n")
        outfile.write(f'{value}: {count} : {percentage:.2f}%\n')
        outfile.write("------------------------\n")
        outfile.write(f"Winner : {winner}")
    # TODO Need to write all the Candidate info in the file and their count.








