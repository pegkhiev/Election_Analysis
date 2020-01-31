#The data we need to retrieve
#1. the total number of votes cast 
#2. A complete list of candidates who receive votes 
#3. The percentage of votes each candidate won 
#4. the total number of votes each candidate won 
#5. The winner of the election based on popular vote

import csv
import os

#assign a variable for the file to load and the path.
file_to_load =  os.path.join("Resources", "election_results.csv")
#Assign a variable for output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize total_vote accumulator as zero 
total_votes = 0

#Candidate options as list 
candidate_options = []

#Declare an empty dictionary for candidates_respective votes 
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Read the file object with the reader function 
with open(file_to_load, newline='') as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row 
    headers = next(file_reader)
    for row in file_reader:
        #2 add to total vote count
        total_votes+=1 
        # print candidate name from each row 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1

for candidate_name in candidate_votes: 
    votes = candidate_votes[candidate_name]
    vote_percentage = votes/total_votes*100
    

    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")      

winning_candidate_summary = (f"-------------------\n" 
f"Winner: {winning_candidate}\n" 
f"Winning Vote Count: {winning_count:,}\n" 
f"Winning Percentage: {winning_percentage:.1f}\n" 
f"--------------------")

print(winning_candidate_summary)









        





    





