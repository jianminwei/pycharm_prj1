import csv

f = open("C:\\dev\\python\\legislators.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

gender = []
for item in legislators:
    gender.append(item[3])

gender = set(gender)
print(gender)