import csv

#Adding a instance method
#Let's make a new method that will always print out the first 10 rows.

class Dataset:
    def __init__(self, data):
        self.data = data

    def print_data(self):
       # New method **remember to add self**.
       print(self.data[:10])

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data()