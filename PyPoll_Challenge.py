

# import dependencies 
import csv
import os

# add a variable to load from file path 
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#iniitialize  a total vote counter 
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

#Challenge county options and county votes 
county_names = []
county_votes = {}

# track the winning cadidiate vote count and percentage
winning_candiate = ""
winning_count = 0
winning_percentage = 0

#Challeneges Track the largest county voter turnout and its percentages 
largest_county_turnout = ""
largest_county_votes = 0

#Read csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    #print(reader)

    #Read the header
    header = next(reader)
    #print(header)

     # for each row in csv file
    for row in reader:
         #dd to the total votes count
        total_votes = total_votes + 1

         # Get the candidate name from each row
        candidate_name = row[2]

         # Extract county name from each row
        county_name = row[1]

         #if the candidate does not match any existing candiate, add it into list
         # the list
        if candidate_name not in candidate_options:
            #add candidate name to list
            candidate_options.append(candidate_name)
            #add begin tracking candidate voter count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate count
        candidate_votes[candidate_name] += 1

        #challenge county
        if county_name not in county_names:

            #challenge add it to list ifn the running
            county_names.append(county_name)
        
            #tracking that candidate voter count 
            county_votes[county_name] = 0
        county_votes[county_name] += 1

#save the result to our text file
with open(file_to_save, "w") as txt_file:
    # print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"\n-------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n-------------------\n\n"
        f"County Votes:\n"
    )    
    print(election_results, end="")
    txt_file.write(election_results)

    # challenge save the final county vote count to the next to the text file 
    for county in county_votes:
        #retrieve vote count and percentage 
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_results, end="")
        txt_file.write(county_results)

        #Determine winning vote count and candidate 
        if (county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county 
    #Print the county with the largest turnout 
    largest_county_turnout = (
        f"\n-------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"----------------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        #retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,}\n"
        )

        print(candidate_results)
        #save candidate result to our text file
        txt_file.write(candidate_results)

        # determine wining vote count winning percentage, and candidate
        if(votes > winning_count) and (vote_percentage >winning_percentage):
            winning_count = votes
            winning_candiate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candiate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n"
    )
    print(winning_candidate_summary)

    #save winning candidate name to the text file 
    txt_file.write(winning_candidate_summary)

 

 







