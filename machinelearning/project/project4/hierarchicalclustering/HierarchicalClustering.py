from sklearn import datasets, metrics
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
iris = datasets.load_iris()

iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                    columns=iris['feature_names'] + ['species'])

print("Data awal iris : ")
print(iris)

iris.columns = iris.columns.str.replace(' ', '')
iris.head()
X = iris.iloc[:, :3]
y = iris.species

sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)

model = AgglomerativeClustering(n_clusters=3)
model.fit(X)
print(model.labels_)

iris['pred_species'] = model.labels_

print("Akurasi : ", metrics.accuracy_score(iris.species, iris.pred_species))
print("Laporan Klasifikasi : ", metrics.classification_report(
    iris.species, iris.pred_species))
