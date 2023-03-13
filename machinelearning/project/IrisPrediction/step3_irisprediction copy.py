import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier   # import algoritma KNN
from sklearn import tree   # import algoritma decision tree

# Mendefinisikan nama-nama kolom dataset
colnames = ["sepal_length", "sepal_width",
            "petal_length", "petal_width", "class"]

# membaca dataset iris dari iris.csv
dataset = pd.read_csv('iris2.csv', header=None, sep=',', names=colnames)

# Meng-encoding kolom yang berkategori text, krn ML hanya mengkalkulasi data numerik
dataset = dataset.replace(
    {"class": {"Iris-setosa": 1, "Iris-versicolor": 2, "Iris-virginica": 3}})

fitur = dataset.iloc[:, 0:4].values
label = dataset.iloc[:, -1].values

# Mengambil algoritma K Nearest Neighbor sebagai model
model = KNeighborsClassifier(n_neighbors=3)

# Latih model menggunakan dataset
model.fit(fitur, label)

# Prediksi dengan data yang dimasukkan
sepal_lengthInput = input("panjang sepal ? \n" + ">>>")
sepal_widthInput = input("lebar sepal ? \n" + ">>>")
petal_lengthInput = input("panjang petal ? \n" + ">>>")
petal_widthInput = input("lebar petal ? \n" + ">>>")
sepallData = float(sepal_lengthInput)
sepalwData = float(sepal_widthInput)
petallData = float(petal_lengthInput)
petalwData = float(petal_widthInput)
prediksinya = model.predict([[sepallData, sepalwData, petallData, petalwData]])
if prediksinya == 1 :
 print("Iris-setosa")
elif prediksinya == 2 :
 print("Iris-versicolor")
elif prediksinya == 3 :
 print("Iris-virginica")
