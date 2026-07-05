import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print(df.shape)  
print(df.head())

print(df.describe())

hayatta_kalan = df[df["Survived"] == 1]
print(hayatta_kalan)
print(len(hayatta_kalan))

print((df["Survived"].value_counts()))

(df["Survived"].value_counts()).plot(kind="bar")
plt.show()

cinsiyet_oran = df.groupby("Sex")["Survived"].value_counts()
print(cinsiyet_oran)

df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df.info())