import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
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

onem = pd.Series(model.feature_importances_, index = x.columns).sort_values(ascending=False)


tahmin = model.predict(x_test)       
olasilik = model.predict_proba(x_test)[:, 1]
gercek = y_test.values

ort = cross_val_score(model, x, y, cv=5)

tablo = pd.DataFrame({
    "gercek": gercek,
    "olasilik": olasilik,
})

yeni_tahmin = (olasilik > 0.30).astype(int)

# print(tablo[:20].round(3))
# print(onem.round(3))
# print(ort.round(3))
# print(round(ort.mean(), 3))
print(classification_report(y_test, tahmin))
print(classification_report(y_test, yeni_tahmin))