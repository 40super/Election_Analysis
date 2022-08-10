# The Data We Need To Retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of election based on popular vote

import csv
import os
#print(dir(csv))
#file_to_load = "resources/election_results.csv"

file_to_load = os.path.join("resources", "election_results.csv")

#election_data = open(file_to_load,'r')
candidate_options = []
total_votes= 0
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#This is a better way to open files using the 'with' keyword

with open(file_to_load) as election_data:
    #TODO Analysis
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] =0
            
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
         votes = candidate_votes[candidate_name]
         # 3. Calculate the percentage of votes.
         vote_percentage = float(votes) / float(total_votes) * 100
         # 4. Print the candidate name and percentage of votes.
         print(f"{candidate_name}: received {vote_percentage}% of the vote.")  
             # Determine winning vote count and candidate
         # Determine if the votes is greater than the winning count.
         print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
         if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
           
         


print(total_votes)    
print(candidate_options)
print(candidate_votes)
# Create a filename variable to a direct or indirect path to the file.

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.







file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
#outfile.write("Hello World")
#outfile.close()
# # Using the with statement open the file as a text file.

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Araphoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")

#TODO : Close files

#election_data.close()