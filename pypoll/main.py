import os
import csv

votes = 0

votes_count = []

candidates = []

csvpath = os.path.join('Resources' , 'election_data.csv')

with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter = ',')

    next(csv_reader)

    for row in csv_reader:
        
        votes = votes + 1
     
        candidate = row[2]
       
        if candidate in candidates:

           candidate_index = candidates.index(candidate)

           votes_count[candidate_index] = votes_count[candidate_index] + 1
        else:
           candidates.append(candidate)

           votes_count.append(1)

    percentages = []

    highest_number_votes = votes_count[0]

    highest_number_votes_index = 0

for count in range(len(candidates)):

    vote_percentage = votes_count[count]/votes*100

    percentages.append(vote_percentage)

    if votes_count[count] > highest_number_votes:
        print(highest_number_votes)

        highest_number_votes_index = count

winner = candidates[highest_number_votes_index]

percentages = [round (i,2) for i in percentages]

print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({votes_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")

#pollfile = os.path.join("analysis", "poll.txt")
with open("poll.txt", "w") as outputfile:

    outputfile.write("Election Results")
    outputfile.write("--------------------------------")
    outputfile.write(f"Total Votes: {votes}")
    outputfile.write("--------------------------------")
for count in range(len(candidates)):
    outputfile.write(f"{candidates[count]:}  {percentages[count]} %{votes_count[count]}")
    outputfile.write("--------------------------------")
    outputfile.write(f"Winner:  {winner}")
    outputfile.write("--------------------------------")
