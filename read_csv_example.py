import pandas as pd

# Read the CSV file
df = pd.read_csv('chicago_venture_funding_data.csv')

# Display the first few rows of the data
print("\nFirst 5 rows of the data:")
print(df.head())

# Display basic information about the dataset
print("\nDataset information:")
print(df.info())

# Display basic statistics of numerical columns
print("\nBasic statistics:")
print(df.describe()) 