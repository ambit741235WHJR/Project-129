# Importing csv
import csv

# Creating an empty list to store the data under variable dataset_1
dataset_1 = []

# Creating an empty list to store the data under variable dataset_2
dataset_2 = []

# Opening the file and reading the data named Brightest Stars.csv under CSVs folder
with open('CSVs/Brightest Stars.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dataset_1.append(row)

# Opening the file and reading the data named Brightest Dwarf Stars.csv under CSVs folder
with open('CSVs/Brightest Dwarf Stars_Cleaned.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dataset_2.append(row)

# Creating a list to store the headers of dataset_1 under variable headers_1 and dataset_2 under variable headers_2
headers_1 = dataset_1[0]
headers_2 = dataset_2[0]

# Creating a list to store the planet data of dataset_1 under variable planets_data_1 and dataset_2 under variable planets_data_2
planets_data_1 = dataset_1[1:]
planets_data_2 = dataset_2[1:]

# Creating a list to store the headers
headers = headers_1 + headers_2

# Creating a list to store the data
planets_data = []

# Using a for loop to append the data from planets_data_1 to planets_data
for i in planets_data_1:
    planets_data.append(i)

# Using a for loop to append the data from planets_data_2 to planets_data
for i in planets_data_2:
    planets_data.append(i)

# Opening the file and writing the data to the file named Total Merged.csv under CSVs folder
with open('CSVs/Total Merged.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(planets_data)