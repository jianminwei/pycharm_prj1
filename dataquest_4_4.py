##################################
# Define a new class: Suspension
# A Suspension instance represent a row from nfl_suspensions

import csv

f = open("C:\\dev\\python\\nfl_suspensions_data.csv", 'r')
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)

nfl_suspensions = nfl_suspensions[1:]

######## training countents################
class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]

    def __str__(self):
        data_string = '[' + self.name + ',' + self.team + ',' + self.games + ',' + self.year + ']'
        return data_string


third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension)