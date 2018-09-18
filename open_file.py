import csv

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

print(nfl_data)