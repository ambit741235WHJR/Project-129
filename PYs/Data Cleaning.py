# Importing pandas
import pandas as pd

# Loading the CSV file named Total Merged.csv inside CSVs folder
df = pd.read_csv("CSVs/Total Merged.csv")

# Dropping the column which is not required
df.drop(columns=['Unnamed: 0', 'Luminosity', 'Unnamed: 6', 'Name.1', 'Radius.1', 'Mass.1', 'Distance.1'], axis=1, inplace=True)

# Dropping the NaN values from the dataframe
df.dropna(inplace=True)

# Reseting the index of the dataframe
df.reset_index(drop=True, inplace=True)

# Exporting the cleaned data to a CSV file named Final Merged Data.csv inside CSVs folder
df.to_csv("CSVs/Final Merged Data.csv", index=True)