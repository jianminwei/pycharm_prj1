# this script is to print out nfl_suspensions_data.csv file to the output
# and we can then copy paste from the output to a notepad.
# This is indirectly download a csv file from the training class.

import csv

f = open("C:\\dev\\python\\nfl_suspensions_data.csv", 'r')
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)

nfl_suspensions = nfl_suspensions[1:]

years = {}

for row in nfl_suspensions:
    # row_year = row[5]
    if row[5] in years:
        years[row[5]] += 1
    else:
        years[row[5]] = 1

print(years)