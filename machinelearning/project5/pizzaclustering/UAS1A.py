from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

Pizza = pd.read_csv('Pizza2.csv', names=[
    'Brand', 'mois', 'prot', 'fat', 'ash', 'sodium', 'carb', 'cal'], header=0)
Pizza = Pizza.replace(
    {"Brand": {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}})

Pizza.columns = Pizza.columns.str.replace(' ', '')
Pizza.head()
X = Pizza.iloc[:, :3].astype(int)
y = Pizza.Brand.astype(int)
sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)

model = KMeans(n_clusters=3, random_state=11)
model.fit(X)

Pizza['pred_Brand'] = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)

fig, ax1 = plt.subplots(2, 2, figsize=(
    22, 18), gridspec_kw={'hspace': 0.5, 'wspace': 0.2})
colorplot = dict({0.0: 'red', 0: 'red', 1.0: 'green',
                 1: 'green', 2.0: 'blue', 2: 'blue',
                 3.0: 'red', 3: 'red', 4.0: 'green',
                 4: 'green', 5.0: 'blue', 5: 'blue',
                 6.0: 'red', 6: 'red', 7.0: 'green',
                 7: 'green', 8.0: 'blue', 8: 'blue',
                 9.0: 'red', 9: 'red', 10.0: 'green',
                 10: 'green'})

sns.scatterplot(data=Pizza, x='mois', y='carb',
                hue='Brand', legend='full', ax=ax1[0, 0], palette=colorplot).set_title('Brand (Actual)')
sns.scatterplot(data=Pizza, x='mois', y='carb',
                hue='pred_Brand', legend='full', ax=ax1[0, 1], palette=colorplot).set_title('Brand (Predicted)')

sns.scatterplot(data=Pizza, x='fat', y='ash',
                hue='Brand', legend='full', ax=ax1[1, 0], palette=colorplot).set_title('Brand (Actual)')
sns.scatterplot(data=Pizza, x='fat', y='ash',
                hue='pred_Brand', legend='full', ax=ax1[1, 1], palette=colorplot).set_title('Brand (Predicted)')

plt.show()
