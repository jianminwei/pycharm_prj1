import csv

##########################
# convert birth_year to integer


f = open("C:\\dev\\python\\legislators.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

for item in legislators:
    # birthday = item[2]
    try:
        birth_year = int(item[2].split('-')[0])
    except Exception:
        birth_year = 0

    item.append(birth_year)

print(legislators)