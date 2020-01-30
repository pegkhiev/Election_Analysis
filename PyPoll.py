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

#Read the file object with the reader function 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row 
    headers = next(file_reader)
    for row in file_reader:
        #2 add to total vote count
        total_votes+=1 
#3 print total votes 
print(total_votes)


        





    





