import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')

# Check the dataset if there's NaN value
print(dataset.isna().values.any())