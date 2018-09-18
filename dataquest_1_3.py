import csv

#Passing additional arguments to the initializer
class Dataset:
    def __init__(self, data):
        self.data = data

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data