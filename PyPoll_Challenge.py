#The data we need to retrieve
#1. the total number of votes cast 
#2. A complete list of candidates who receive votes 
#3. The percentage of votes each candidate won 
#4. the total number of votes each candidate won 
#5. The winner of the election based on popular vote

#CHALLENGE
#The data to be retrieved: 
#1. A complete list of counties that casted votes 
#2. Each county's total vote count 
#3. Each county's percentage of total votes 
#4. County with the largest number of voters 

import csv
import os

#assign a variable for the file to load and the path.
file_to_load =  os.path.join("Resources", "election_results.csv")
#Assign a variable for output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total_vote accumulator as zero 
total_votes = 0

#Candidate options as list 
candidate_options = []

#Declare an empty dictionary for candidates_respective votes 
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Initialize county_names list 
county_names = []

#Initialize county_votes empty dictionary
county_votes = {} 

#Create empty string for largest county turnout
#Create variable for number of votes, and percentage of votes of the largest county 
largest_county = ""
largest_count = 0
largest_percentage = 0

#Read the file object with the reader function 
with open(file_to_load, newline='') as election_data:
    file_reader = csv.reader(election_data)
    #read and print the header row 
    headers = next(file_reader)
    for row in file_reader:
        # add to total vote count
        total_votes+=1 
        # print candidate name from each row 
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            #candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1
    
#CHALLENGE 
        #1. In the same for loop, index county name from each row 
        county_name = row[1]
        #2. Collect total votes per county 
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] +=1
    #print(county_votes)

with open(file_to_save, "w", newline='') as txt_file:
    election_results = (f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    f"\nCounty Votes:\n")
    print(election_results)
    txt_file.write(election_results)

    #3. calculate county vote percentage
    for county_name in county_votes:
        total_county_votes = county_votes[county_name]
        total_county_percentage = county_votes[county_name]/total_votes*100

    #print county votes summary
    
        county_summary = (f"{county_name}: {total_county_percentage:.1f}% ({total_county_votes:,})\n")
        print(county_summary)
        txt_file.write(county_summary)

    #4 determine the largest county turnout
        if (total_county_votes> largest_count) and (total_county_percentage > largest_percentage):
            largest_count = total_county_votes
            largest_percentage = total_county_percentage
            largest_county = county_name

    #print largest county turnout result
    largest_county_turnout = (f"\n-------------------------\n"
    f"Largest County Turnout: {largest_county}\n"
    f"-------------------------\n")
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percentage = votes/total_votes*100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


    

    winning_candidate_summary = (f"-------------------------\n" 
        f"Winner: {winning_candidate}\n" 
        f"Winning Vote Count: {winning_count:,}\n" 
        f"Winning Percentage: {winning_percentage:.1f}%\n" 
        f"-------------------------")


    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)










        





    





