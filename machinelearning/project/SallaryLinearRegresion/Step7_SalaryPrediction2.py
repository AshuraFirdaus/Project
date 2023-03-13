import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Get Linear Regression as model and training the model using X, y data
regressor = LinearRegression()
regressor.fit(X, y)

# Please predict how much salary for input of years of experience
tahunInput = input("Berapa tahun pengalaman anda bekerja ? \n" + ">>>")
tahunData = float(tahunInput)
y_pred = regressor.predict([[tahunData]]) # Predicting the input data set results
print("Perkiraan Gaji anda adalah : {}".format(y_pred))