# Untuk Jawaban 1C dan 2B
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import numpy as np
import csv as csv

st.sidebar.header('User Input Parameters')


def user_input_features():
    st.sidebar.write(
        "Gerakan slider untuk mengatur parameter")
    mois = st.sidebar.slider('mois', 43.0, 55.9, 51.0)
    prot = st.sidebar.slider('prot', 5.0, 20.0, 13.5)
    fat = st.sidebar.slider('fat', 15.0, 40.0, 25.0)
    ash = st.sidebar.slider('ash', 0.1, 5.5, 3.5)
    sodium = st.sidebar.slider('sodium', 0.1, 5.5, 1.0)
    carb = st.sidebar.slider('carb', 0.1, 7.5, 4.5)
    cal = st.sidebar.slider('cal', 0.1, 7.5, 3.0)
    data = {'mois': mois, 'prot': prot,
            'fat': fat, 'ash': ash,
            'sodium': sodium, 'carb': carb, 'cal': cal}
    features = pd.DataFrame(data, index=[0])
    return features


option_clf = st.sidebar.selectbox("How would you like classification algorithm to be used?", (
    'Naive Bayes', 'Nearest Neighbor', 'Support Vector Machine', 'Random Forest', 'Decision Tree'))

colnames = ["Brand", "mois", "prot",
            "fat", "ash",
            "sodium", "carb", "cal"]

# quoting=csv.QUOTE_NONNUMERIC, skiprows=1)
dataset = pd.read_csv('Pizza2.csv', header=None, sep=',', names=colnames,)

#dataset['Brand'] = dataset['Brand'].convert_objects(convert_numeric=True)
#dataset['Brand'] = dataset.Brand.astype(int)
#dataset = dataset.apply(pd.to_numeric, axis=0)
#dataset = dataset.apply(pd.to_numeric, errors='coerce')
#dataset["mois"] = [float(str(i).replace(",", "")) for i in dataset["mois"]]
#dataset["prot"] = [float(str(i).replace(",", "")) for i in dataset["prot"]]
#dataset["fat"] = [float(str(i).replace(",", "")) for i in dataset["fat"]]
#dataset["ash"] = [float(str(i).replace(",", "")) for i in dataset["ash"]]
#dataset["sodium"] = [float(str(i).replace(",", "")) for i in dataset["sodium"]]
#dataset["carb"] = [float(str(i).replace(",", "")) for i in dataset["carb"]]
#dataset["cal"] = [float(str(i).replace(",", "")) for i in dataset["cal"]]
#dataset["Brand"] = [float(str(i).replace(",", "")) for i in dataset["Brand"]]
#dataset = dataset.replace('[^\d.]', '', regex=True).astype(float)


st.subheader("The sample of origin dataset is :")
st.write(dataset.sample(frac=0.2))

st.subheader("Plotting the mois v carb and fat v ash features data are :")
colorplot = dict(
    {'A': 'red', 'B': 'green', 'C': 'blue', 'D': 'yellow', 'E': 'brown', 'F': 'orange', 'G': 'purple', 'H': 'pink', 'I': 'grey', 'J': 'white',  'Brand': 'black'})

moiscarb = plt.figure(1)
sns.scatterplot(data=dataset, x='mois', y='carb', hue='Brand',
                legend='full', palette=colorplot).set_title('mois carb')
st.write(moiscarb)

fatash = plt.figure(2)
sns.scatterplot(data=dataset, x='fat', y='ash', hue='Brand',
                legend='full', palette=colorplot).set_title('fat ash')
st.write(fatash)

dataset = dataset.replace(
    {"Brand": {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}})
st.subheader(
    "The sample of dataset which the class column replace by numeric :")
st.write("Because the ML only calculate the numeric data, so we encode the class data to numeric")
st.write(dataset.sample(frac=0.2))

st.subheader("User Input Parameters")
user_input_param = user_input_features()
st.write(user_input_param)

X = dataset.iloc[:, :-1].astype("int")
y = dataset.iloc[:, -1].values.astype("int")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)

st.subheader("Classification Model to be choosen :")
st.write(option_clf)
if option_clf == "Naive Bayes":
    model = GaussianNB()
elif option_clf == "Nearest Neighbor":
    model = KNeighborsClassifier(n_neighbors=3)
elif option_clf == "Support Vector Machine":
    model = SVC(kernel='linear', random_state=0)
elif option_clf == "Random Forest":
    model = RandomForestClassifier()
elif option_clf == "Decision Tree":
    model = tree.DecisionTreeClassifier()
else:
    model = SVC(kernel='linear', random_state=0)

model.fit(X, y)

prediction = model.predict(user_input_param)

st.subheader(
    'Class labels and their corresponding index number of prediction :')
st.write(prediction)
type_flower = {1: "A", 2: "B", 3: "C", 4: "D",
               5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"}
st.subheader("Index number & label prediction : {}--> {} ".format(
    prediction[0], type_flower[prediction[0]]))

st.subheader("The accuracy of prediction :")
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
st.write("The confusion matrix is:")
st.write(cm)

accuracies = cross_val_score(estimator=model, X=X_train, y=y_train, cv=10)
accuracies2 = accuracy_score(y_test, y_pred)
st.write("Accuracy using cross_val_score: {:.2f} %".format(
    accuracies.mean() * 100))
st.write("Accuracy using accuracy_score: {:.2f} %".format(accuracies2 * 100))
st.write("Standard Deviation: {:.2f} %".format(accuracies.std() * 100))
