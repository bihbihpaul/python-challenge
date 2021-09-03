import os
import csv

filepath = os.path.join('Resources' , 'budget_data.csv')

with open(filepath,'r') as f:
    csv_reader = csv.reader(f, delimiter = ',')

    for row in csv_reader:
        print(row)

