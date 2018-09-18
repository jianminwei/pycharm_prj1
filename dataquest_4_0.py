# this script is to print out nfl_suspensions_data.csv file to the output
# and we can then copy paste from the output to a notepad.
# This is indirectly download a csv file from the training class.

import csv

f = open("nfl_suspensions_data.csv", 'r')
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)

#print (len(nfl_suspensions))

for row in nfl_suspensions:
    # join each item in the row by "," (this is for delimited csv file)
    s='","'
    s=s.join(row)
    # add beginnin and ending "
    s='"' + s + '"'
    print(s)