# The data we need to retrieve
# 1. total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. Winner of election based on popular vote

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

#Declare new list
candidate_options = []

# Declare the empty dictionary
candidate_votes= {}

#Open the eletion results and read the file
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print header row
    headers = next(file_reader)

    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidat name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add candidate name to candidate list
            candidate_options.append(candidate_name)   

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Print the candidate list
print(candidate_votes)
