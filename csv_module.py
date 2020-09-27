# How to read, parse, and write CSV files

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        
        for line in csv_reader:
            assert isinstance(csv_writer, object)
            csv_writer.writerow(line)


with open('names.csv', 'r') as csv_file:
    csv_reader= csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)