##################################
# List comprehension
# Set to get unique

import csv

f = open("C:\\dev\\python\\nfl_suspensions_data.csv", 'r')
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)

nfl_suspensions = nfl_suspensions[1:]

######## training countents################
teams = [row[1] for row in nfl_suspensions]
unique_teams = set(teams)

games = [row[2] for row in nfl_suspensions]
unique_games = set(games)

print(unique_teams)
print(unique_games)