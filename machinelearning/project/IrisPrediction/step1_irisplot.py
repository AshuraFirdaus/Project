import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

irisDataset = pd.read_csv('iris.csv', names=['sepal-length','sepal-width','petal-length','petal-width','label'], header=0, sep=",")
sns.scatterplot(x='sepal-length',y='sepal-width',hue='label', data=irisDataset).set_title('jenis bunga iris')
plt.figure(1)
plt.show()