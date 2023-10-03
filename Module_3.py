import os
import csv

#Initialize Varialbes
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes = []
dates = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

#Read in CSV
csv_file = "budget_data.csv"

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #Extract Data from Row
        date = row[0]
        profit_loss = int(row[1])
        #Calcultate total number of months and net total
        total_months += 1
        total_profit_losses += profit_loss
       
       #Calculate the change in Profit & Loss compared to previous
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
            #Check for greatest increase & decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        #Update for next Iteration
        previous_profit_loss = profit_loss

#Calculate Average
average_change = sum(changes) / len(changes)

#Print Results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")



#Initalize Variables
total_votes = 0
candidate_votes = {}
candidates = []

#Read in CSV file
csv_file = "election_data.csv"

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #Extract Data from Row
        voter_id = row[0]
        candidate = row[2]
        #Calculate total Number of Rows
        total_votes += 1
        #Count the Votes of each Candidate       
        if candidate not in candidates:
            candidates.append(candidate)
       
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
#Calculate percentage of votes that each candidate won 
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
#Determine the winner 
winner = max(candidate_votes, key=candidate_votes.get)
#Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



