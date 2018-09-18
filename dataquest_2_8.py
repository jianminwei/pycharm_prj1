import csv

##########################
# convert birth_year to integer

###############################
# pass the exception in the int() conversion

f = open("C:\\dev\\python\\legislators.csv", 'r')
csvreader = csv.reader(f)
legislators = list(csvreader)

birth_years = []

for item in legislators:
    birthday = item[2]
    birthday_parts = birthday.split("-")
    birth_years.append(birthday_parts[0])

converted_years = []

for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except Exception:
        pass

print(converted_years)