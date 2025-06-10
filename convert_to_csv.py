import pandas as pd

# Read the Excel file
df = pd.read_excel('chicago_venture_funding_data.xlsx')

# Save as CSV
df.to_csv('chicago_venture_funding_data.csv', index=False)

print("Conversion completed successfully!") 