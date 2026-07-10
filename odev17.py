import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())

cinsiyetler = df["Sex"]
sns.countplot(data=df, x="Sex", hue="Survived")
plt.show()


# data=df verdiğin için. Seaborn data parametresine bir DataFrame verince, x ve hue'ya sadece kolon adını string olarak yazman yeterli
# geri kalanını kendisi hallediyor. df["Sex"] yazmana gerek kalmıyor çünkü zaten df'in içinde arıyor.