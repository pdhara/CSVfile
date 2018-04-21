#To make use of the functions in a module, you'll need to import the module with an import statement.
import csv

#open the csv file and read the file out to a variable
with open('config.csv' , 'r') as csv_f:
    read = csv.reader(csv_f)
    for row in read:
        print(row[0])
        print(row[2])
