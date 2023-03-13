import streamlit as st
from PIL import Image
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

st.write(""" # Simple Iris Flower Prediction App
## This App Predicts the **Iris Flower** Type with Some Classification Algorithm! """)


image = Image.open('iris.png')
st.image(image, caption='Iris flowers type', use_column_width=True)

st.sidebar.header('User Input Parameters')


def user_input_features():
    st.sidebar.write(
        "Move the slider to change input parameter of sepal & petal.")
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length, 'sepal_width': sepal_width,
            'petal_length': petal_length, 'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


option_clf = st.sidebar.selectbox("How would you like classification algorithm to be used?", (
    'Naive Bayes', 'Nearest Neighbor', 'Support Vector Machine', 'Random Forest', 'Decision Tree'))

colnames = ["sepal_length", "sepal_width",
            "petal_length", "petal_width", "class"]

dataset = pd.read_csv('iris.csv', header=None, sep=',', names=colnames)

st.subheader("The sample of origin dataset is :")
st.write(dataset.sample(frac=0.2))

st.subheader("Plotting the sepal and petal features data are :")
colorplot = dict(
    {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'})

sepalfig = plt.figure(1)
sns.scatterplot(data=dataset, x='sepal_length', y='sepal_width', hue='class',
                legend='full', palette=colorplot).set_title('Sepal Feature')
st.write(sepalfig)

petalfig = plt.figure(2)
sns.scatterplot(data=dataset, x='petal_length', y='petal_width', hue='class',
                legend='full', palette=colorplot).set_title('Petal Feature')
st.write(petalfig)

dataset = dataset.replace(
    {"class": {"Iris-setosa": 1, "Iris-versicolor": 2, "Iris-virginica": 3}})
st.subheader(
    "The sample of dataset which the class column replace by numeric :")
st.write("Because the ML only calculate the numeric data, so we encode the class data to numeric")
st.write("Iris-setosa:1 | Iris-versicolor:2 | Iris-virginica:3")
st.write(dataset.sample(frac=0.2))

st.subheader("The Heatmap of dataset :")
heatmapfig = plt.figure(3)
sns.heatmap(dataset.corr()).set_title("Correlation On iris Classes")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
st.write(heatmapfig)
st.write(""" As we can see, the shape of the petals (petal_length and petal_width) are the most correlationed columns with the type of flowers, with lower correlation there is the sepal length wich also haves a  directly correlation and in last place there we have the negative correlation of the sepal width column, but this doen't mean that is less important, is important but is inverse relationed with the type of flower. And as we can see at scatter plot picture too, petal features almost perfect classified. """)

st.subheader("User Input Parameters")
user_input_param = user_input_features()
st.write(user_input_param)

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1].values
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
type_flower = {1: "iris-setosa", 2: "iris-versicolor", 3: "iris-virginica"}
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
