##################################
# Define a new class: Suspension
# A Suspension instance represent a row from nfl_suspensions

import csv

f = open("C:\\dev\\python\\nfl_suspensions_data.csv", 'r')
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)

nfl_suspensions = nfl_suspensions[1:]

######## training countents################
class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]

        try:
            year = int(row[5])
        except Exception:
            year = 0
        self.year = year

    def get_year(self):
        return self.year


missing_year = Suspension(nfl_suspensions[22])

twenty_third_year = missing_year.get_year()

print(twenty_third_year)