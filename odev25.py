import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score



df = pd.read_csv("train.csv")
df["Sex"] = df["Sex"].map({"male":0, "female":1})
df = df.dropna(subset=["Embarked"])
df["Embarked"] = df["Embarked"].map({"S":3, "C":4, "Q":5})
df["Age"] = df["Age"].fillna(df["Age"].mean())


x = df.drop(columns=["Survived","Name", "Ticket", "Cabin", "PassengerId"])
y = df["Survived"]




x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=67)

model = RandomForestClassifier(random_state=67)
model.fit(x_train, y_train)


yeni_yolcu = pd.DataFrame({
    "Pclass": [3,1],
    "Sex":[0,1],
    "Age":[8,23],
    "SibSp":[1,1],
    "Parch":[1,1],
    "Fare":[18,18],
    "Embarked":[3,3]
   
})



tahmin = model.predict(x_test)       
olasilik = model.predict_proba(x_test)[:, 1]
olasilik_yeni = model.predict_proba(yeni_yolcu)[:, 1]
gercek = y_test.values

ort = cross_val_score(model, x, y, cv=5)

tablo = pd.DataFrame({
    "gercek": gercek,
    "olasilik": olasilik,
})

print(olasilik_yeni)

