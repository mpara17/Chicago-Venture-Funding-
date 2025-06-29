# -*- coding: utf-8 -*-
"""MS-ADS Code

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15d-Q90IPD5xzCOI7fBm1V3bWh-95oRfw
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#read in the data
df = pd.read_csv('chicago_venture_funding_data.csv')
df

df.head()
df.info()
df.describe()

# data wrangling
df['Stage'] = df['Stage'].astype('category')
df['Sector'] = df['Sector'].astype('category')
df.info()

# create a function to plot the total funding by a given column
def plot_total_funding(df, col):
    df.groupby(col)['Amount Raised ($M)'].sum().sort_values().plot(
        kind='barh', figsize=(8, 5), color='skyblue', title=f'Total Funding by {col}'
    )
    plt.xlabel("Amount Raised ($M)")
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.show()

# plot the total funding by lead investor
plot_total_funding(df, 'Lead Investor')

# plot the total funding by sector
plot_total_funding(df, 'Sector')

# plot the total funding by stage
plot_total_funding(df, 'Stage')
