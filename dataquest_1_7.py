import csv

#############################
#Adding a count_unique method

############################
# How to call other instance method
#def other_instance_method(self):
#    results = self.get_results()
#    ...
#...

#####################
#  To return a unique set of items from a list, we can use the set() function

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

    def count_unique(self, label):
        #call column instance method
        return(len(set(self.column(label))))

f = open("C:\\dev\\python\\nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)

year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

print(year_column)
print(player_column)