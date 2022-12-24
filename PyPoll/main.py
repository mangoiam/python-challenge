# Import dependencies
import os, csv

# Assign file location with the pathlib library
csv_file_path = os.path.join('Resources', 'election_data.csv')

count_diana = 0
count_raymon = 0
count_charles = 0

voterids = []
all_candidates = []
odd_candidate = []

with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next (csvreader)

    for row in csvreader:
        voterids.append(int(row[0]))
        all_candidates.append(row[2])

        candidate = row[2]
        if candidate not in odd_candidate:
            odd_candidate.append(candidate)

for i in odd_candidate:
    if i == "Raymon Anthony Doane":
        count_raymon = count_raymon + 1

    elif i == "Charles Casper Stockham":
        count_charles = count_charles + 1

    else:
        count_diana = count_diana + 1

total_votes = (len(voterids))
percent_diana = str(round(count_diana/total_votes * 100, 3)) + "%"
percent_raymon = str(round(count_raymon/total_votes * 100, 3)) + "%"
percent_charles = str(round(count_charles/total_votes * 100, 3)) + "%"


if percent_diana < percent_raymon and percent_charles < percent_raymon:
    winner = "Raymon Anthony Doane"

elif percent_raymon < percent_diana and percent_charles < percent_diana:
    winner = "Diana DeGette"

else:
    winner = "Charles Casper Stockham"



print("Election Results")
print("-------------------")
print(f"Total votes: {total_votes}")
print("-------------------")
print(f"Charles Casper Stockham: {percent_charles} ({count_charles})")
print(f"Diana DeGette: {percent_diana} ({count_diana})")
print(f"Raymon Anthony Doane: {percent_raymon} ({count_raymon})")
print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

with open ('./analysis.txt' , 'w') as file:

    file.write("Election Results\n")
    file.write("-------------------\n")
    file.write(f"Total votes: {total_votes}\n")
    file.write(f"-------------------\n")
    file.write(f"Charles Casper Stockham: {percent_charles} ({count_charles})\n")
    file.write(f"Diana DeGette: {percent_diana} ({count_diana})\n")
    file.write(f"Raymon Anthony Doane: {percent_raymon} ({count_raymon})\n")
    file.write("-------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------\n")
    file.close()