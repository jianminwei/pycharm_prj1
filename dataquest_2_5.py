import csv

# using split() to split date into date parts, and extract date parts.
f = open("C:\\dev\\python\\legislators.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

birth_years = []

for item in legislators:
    birthday = item[2]
    birthday_parts = birthday.split("-")
    birth_years.append(birthday_parts[0])

print(birth_years)