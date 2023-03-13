import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Get Linear Regression as model and training the model using X_train, y_train data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# How much accuracy of the model
akurasi = regressor.score(X_train, y_train)
print("Akurasi dari model adalah : {}".format(akurasi))
print("Nilai gradient : ", regressor.intercept_)
print("Nilai koefisien : ", regressor.coef_)

# Visualising the Training set results
plt.figure(1) #n must be a different integer for every window
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

# Visualising the Test set results
plt.figure(2) #n must be a different integer for every window
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show() # dengan matplotlib figure semua window digambar dan ditampilkan melalui plt.show()
