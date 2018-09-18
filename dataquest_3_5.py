import csv

##########################
# Let's count how many times each female first name occurs in legislators.
# To limit our count to names from the modern era, we'll only look at those that appear after 1940

f = open("C:\\dev\\python\\legislators2.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

name_counts = {}

for item in legislators:
    try:
        year = int(item[7])
    except Exception:
        year = 0

    if item[3] == 'F' and year > 1940 :
        name = item[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1