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

file_to_save = os.path.join("analysis", "election_analysis.txt")
#Read the file object with the reader function 
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   headers = next(file_reader)
   print(headers)
   



    





