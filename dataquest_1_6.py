import csv

#Adding a column method

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def print_data(self, row):
       # New method **remember to add self**.
       print(self.data[1:1+1])

    def print_header(self):
       # New method **remember to add self**.
       print(self.header)

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)

year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

print(year_column)
print(player_column)