import csv
import pandas as pd

dataset1 = []
dataset2 = []

with open("bright_stars.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset1.append(i)

with open("sorted_dwarf_stars.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset2.append(i)

headers = dataset1[0]
data1 = dataset1[1:]
data2 = dataset2[1:]

for i in data2:
    data1.append(i)

with open("merged_stars.csv", 'a+') as f:
    dataset_sorted = csv.writer(f)
    dataset_sorted.writerow(headers)
    dataset_sorted.writerows(data1)



