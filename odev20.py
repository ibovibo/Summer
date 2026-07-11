import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")
df.drop(columns=["Cabin", "Ticket", "Name", "PassengerId"], inplace = True)
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["aile_boyutu"] = df["SibSp"] + df["Parch"] +1


df["yas_grubu"] = pd.cut(df["Age"],
                       bins = [0, 12, 25, 60, 120],
                       labels = ["cocuk", "genc", "yetiskin", "yasli"])


hayatta_kalan = df["Survived"]

(df["Survived"].value_counts()).plot(kind="bar")
plt.show()


cinsiyetler = df["Sex"]
sns.countplot(data=df, x="Sex", hue="Survived")
plt.show()


yaslar = df["Age"]
plt.hist(yaslar, bins=5)
plt.title("Yas Dagilimi")
plt.xlabel("yas")
plt.ylabel("kisi sayisi")
plt.show()

sinifsal_yasam = df["Pclass"]
sns.countplot(data = df, x="Pclass", hue="Survived")
plt.show()