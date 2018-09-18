import csv

# Data Clensing. replace missing gender by 'M'
f = open("C:\\dev\\python\\legislators.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

gender = []
for item in legislators:
    if item[3] == '':
        item[3] = 'M'
    gender.append(item[3])

gender = set(gender)
print(gender)