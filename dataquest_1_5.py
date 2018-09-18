import csv

#Adding a header method

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

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_header()