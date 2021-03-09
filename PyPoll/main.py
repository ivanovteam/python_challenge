 
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# defining the path to the election_data.csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')


# creating variables,lists and a dictionary
count = 0
candidate = []
total = 0
average = 0
i = 0
candidate_vote = {}
percentage = []
  
#  Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # counts the total amount of rows
    for row in csvreader:
        # counts the total amount of rows
        count += 1
        #creates a list with all the candidates' names
        candidate=row[2]
        # counts all the votes for each candidate
        if candidate in candidate_vote.keys():
            candidate_vote[candidate] += 1
        else:
            candidate_vote[candidate]=1
#    prints the header and the total amounts of votes
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {count}")
    print("----------------------------")
   
    # calculates and prints the result for each candidate as percentage and total votes per each
    for i in candidate_vote:
        
        percentage = (candidate_vote[i]/count)*100
        
        print(f"{i} {round(percentage,2)}% {candidate_vote[i]}")   

    # printing the winner
    print("----------------------------")
    print(f"Winner:", max(candidate_vote, key=lambda key: candidate_vote[key]))
    print("----------------------------")
    
  
# creates an analysis file in the analysis folder
output_file = os.path.join('..', 'analysis','analysis.csv')

#  Open the output file
with open(output_file, "w") as datafile:   
    # writes all the amounts in the file formated the same way as in the printing.
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total votes: {count}\n")
    datafile.write("----------------------------\n")
    
    for i in candidate_vote:

        percentage = (candidate_vote[i]/count)*100
        datafile.write(f"{i} {round(percentage,2)}% {candidate_vote[i]}\n")
    # printing the winner
    datafile.write("----------------------------\n")
    datafile.write(f"Winner:{ max(candidate_vote, key=lambda key: candidate_vote[key])}\n")
    datafile.write("----------------------------\n")