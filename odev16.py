import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())

yaslar = df["Age"]
plt.hist(yaslar, bins=5)
plt.title("Yas Dagilimi")
plt.xlabel("yas")
plt.ylabel("kisi sayisi")
plt.show()