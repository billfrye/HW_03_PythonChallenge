
#%%
# import dependencies
import os
import csv


#%%
# Create input and output filenames
file_path = os.path.join('.','Resources','election_data.csv')
output_path = os.path.join('.','output_file.txt')


#%%
# setup a few needed variables
total_num_votes = 0

# Each candidate that receives a vote will have a dictionary entry with their
# vote count.
vote_totals = {}

# start processing loop...
with open(file_path) as file:
    reader = csv.reader(file, delimiter = ',')
    # skip the header row
    header = next(reader)
#     print(f'header = {header}')
    for row in reader:
        total_num_votes = total_num_votes + 1 # bump the vote count
        person = row[2]
        if (person in vote_totals):
            vote_totals[person] = vote_totals[person] + 1
        else:
            vote_totals[person] = 1 # first time voted for, no key will be there          


#%%
# format the output
width = 70
dashes = " -----------------------------"
summary_strs = [
    "\n Election Analysis".ljust(width," "),
    dashes.ljust(width, " "),
    " Total Votes: {:,.0f}".ljust(width, " ").format(total_num_votes),
    dashes.ljust(width, " "),
]


#%%
winner = "" # will indicate the winner
winner_votes = 0
for k in vote_totals.keys():
    v = vote_totals[k]
    s = " {}: {:.3%} ({:,.0f})".format(k, v/total_num_votes, v)
    summary_strs.append( s )
    if (v > winner_votes):
        winner_votes = v
        winner = k

summary_strs.append(dashes.ljust(width," "))
summary_strs.append(f' Winner: {winner}')
summary_strs.append(dashes.ljust(width," "))

for s in summary_strs:
    print(s)


#%%
#write to output_file.txt


#%%
str_array_to_prt = summary_strs
data_path = output_path
with open(data_path, 'w+') as outfile:
    for s in str_array_to_prt :
        outfile.write(s + '\n')


