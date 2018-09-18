import csv

##########################
# fill missing birth_year with previous row value

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

last_value = 1
for item in legislators:
    if item[7] == 0:
        item[7] = last_value
    else:
        last_value = item[7]

print(legislators)