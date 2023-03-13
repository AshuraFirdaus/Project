import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values # independent variable
y = dataset.iloc[:, 1].values # dependent variable

# Get Linear Regression as model and apply the model using X, y data
lr = LinearRegression()
lr.fit(X, y)

# add predict value to the dataframe
dataset['Salary_Pred'] = lr.predict(X)

#print(dataset['Test_Salary_Pred'])
# Manually calculating R-Squared
dataset['SST'] = np.square(dataset['Salary'] - dataset['Salary'].mean())
dataset['SSR'] = np.square(dataset['Salary_Pred'] - dataset['Salary'].mean())
print("Sum of SSR : ", dataset['SSR'].sum())
print("Sum of SST : ", dataset['SST'].sum())
print("R Squared using manual calculation : ", dataset['SST'].sum()/dataset['SST'].sum())

# Using built-in function
print("R Squared using built-in function : ", lr.score(X, y))
print("Mean Absolute Error (MAE) : ", mean_absolute_error(y, dataset['Salary_Pred']))
print("Root Mean Squared Error : ", np.sqrt(mean_squared_error(y, dataset['Salary_Pred'])))

# Check the correlation between variables
print("Correlation Matrix : ")
print(dataset.corr())