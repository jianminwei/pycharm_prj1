import csv

#############################
#Adding a __str__ method
#
# Every class should define a __str__() method as a good practice

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def __str__(self):
        data_string = self.data[:10]
        return str(data_string)

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

    def count_unique(self, label):
        #call column instance method
        return(len(set(self.column(label))))

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)

print(nfl_dataset)