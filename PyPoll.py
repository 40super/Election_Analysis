# The Data We Need To Retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of election based on popular vote
import csv
import os

print(dir(csv))
#file_to_load = "resources/election_results.csv"
file_to_load = os.path.join("resources", "election_results.csv")
#election_data = open(file_to_load,'r')

#This is a better way to open files using the 'with' keyword

with open(file_to_load) as election_data:
    #TODO Analysis
    file_reader = csv.reader(election_data)
    #for row in file_reader:
    #    print(row)
    headers = next(file_reader)
    print(headers)
    
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.

#outfile = open(file_to_save, "w")
#outfile.write("Hello World")
#outfile.close()
# # Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Araphoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")

#TODO : Close files

#election_data.close()