# Importing pandas
import pandas as pd

# Loading the CSV file named Brightest Dwarf Stars.csv inside CSVs folder
df = pd.read_csv("CSVs/Brightest Dwarf Stars.csv")

# Cleaning the data by deleting blank values from the list of stars data of dataset_1
df = df[df['Name'].notna()]
df = df[df['Radius'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Distance'].notna()]

# Converting the Radius and Mass Column to the floating point values
df['Radius'] = df['Radius'].astype(float)
df['Mass'] = df['Mass'].astype(float)

# Multiplying each value in the radius column with 0.102763 to convert to solar radius
df['Radius'] = df['Radius'] * 0.102763

# Multiplying each value in the mass column with 0.000954588 to convert to solar mass
df['Mass'] = df['Mass'] * 0.000954588

# Dropping the column Unnamed: 0
df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

# Reseting the index of the dataframe
df.reset_index(drop=True, inplace=True)

# Exporting the cleaned data to a CSV file named Brightest Dwarf Stars_Cleaned.csv inside CSVs folder
df.to_csv("CSVs/Brightest Dwarf Stars_Cleaned.csv", index=True)