import csv

##########################
# Caculate the max common female first name after 1940

f = open("C:\\dev\\python\\legislators2.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

name_counts = {}

for item in legislators:
    #if item[3] == 'F' and int(item[7]) > 1940 :
    if item[3] == 'F' :
        name = item[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

max_value = None

for name in name_counts:
    count = name_counts[name]

    if max_value is None or count > max_value:
        max_value = count

print(max_value)