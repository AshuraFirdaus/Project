import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

irisDataset = pd.read_csv('iris.csv', names=['petal-length', 'petal-width', 'class'], header=0)
fitur = irisDataset.iloc[:, 0:2].values
label = irisDataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(fitur, label, test_size= 1/3, random_state = 0)
print("Data training:")
print(X_train)
print("Data test:")
print(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

akurasi = model.score(X_train, y_train)
print("Akurasi dari model adalah : {}".format(akurasi))
