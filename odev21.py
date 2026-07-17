import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("train.csv")
df["Sex"] = df["Sex"].map({"male":0, "female":1})
df = df.dropna(subset=["Embarked"])
df["Embarked"] = df["Embarked"].map({"S":3, "C":4, "Q":5})

df["Age"] = df["Age"].fillna(df["Age"].mean())



x = df.drop(columns=["Survived","Name", "Ticket", "Cabin"])
y = df["Survived"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

print(model.score(x_test, y_test))


# Titanic'te 889 yolcu var. train_test_split bunları rastgele ikiye bölüyor:

# x_train + y_train → ~711 yolcu (%80) — eğitim
# x_test + y_test → ~178 yolcu (%20) — test

# İkisi de aynı train.csv'den geliyor, sadece ayrı gruplara bölünmüş. Ayrı bir dosya değil.
# Yani test verisi = kendi verinin, modelden sakladığın %20'lik kısmı. 
# Model onları eğitimde hiç görmüyor, o yüzden "yeni veri" gibi davranıyor. 
# Sınav mantığı: 889 soruluk kitabın 711'iyle çalış, kalan 178'iyle kendini sına.