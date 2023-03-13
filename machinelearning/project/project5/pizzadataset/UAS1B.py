from sklearn import datasets, metrics
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

Pizza = pd.read_csv('Pizza2.csv', names=[
    'Brand', 'mois', 'prot', 'fat', 'ash', 'sodium', 'carb', 'cal'], header=0)
Pizza = Pizza.replace(
    {"Brand": {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}})

print("Data awal Pizza : ")
print(Pizza)

Pizza.columns = Pizza.columns.str.replace(' ', '')

Pizza.head()

X = Pizza.iloc[:, :3]
y = Pizza.Brand
sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)

model = KMeans(n_clusters=3, random_state=11)
model.fit(X)
print("label hasil clustering KMeans adalah :")
print(model.labels_)
Pizza['pred_Brand'] = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)
print("Accuracy :", metrics.accuracy_score(Pizza.Brand, Pizza.pred_Brand))
print("Classification report :", metrics.classification_report(
    Pizza.Brand, Pizza.pred_Brand))
print("homogeneity score : ", metrics.homogeneity_score(
    y, Pizza['pred_Brand']))
print("homogeneity, completeness, v -measure: ",
      metrics.homogeneity_completeness_v_measure(y, Pizza['pred_Brand'], beta=1.0))
print("Cetak data Pizza dengan full rows:")
pd.set_option('display.max_rows', None)
print(Pizza)
print("Cetak data Pizza dengan sampel acak sebesar 0,3 :")
print(Pizza.sample(frac=0.3))
