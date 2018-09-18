import csv

#Passing additional arguments to the initializer
f = open("C:\\dev\\python\\legislators.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

party = []
for item in legislators:
    party.append(item[6])

party = set(party)
print(party)
print(legislators)