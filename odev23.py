import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("train.csv")
df["Sex"] = df["Sex"].map({"male":0, "female":1})
df = df.dropna(subset=["Embarked"])
df["Embarked"] = df["Embarked"].map({"S":3, "C":4, "Q":5})

df["Age"] = df["Age"].fillna(df["Age"].mean())



x = df.drop(columns=["Survived","Name", "Ticket", "Cabin", "PassengerId"])
y = df["Survived"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=67)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


model = DecisionTreeClassifier(random_state=67)
model.fit(x_train, y_train)

model2 = RandomForestClassifier(random_state=67)
model2.fit(x_train, y_train)

model3 = KNeighborsClassifier()
model3.fit(x_train_scaled, y_train)


print(model.score(x_test, y_test))
print(model2.score(x_test, y_test))
print(model3.score(x_test_scaled, y_test))

y_pred = model2.predict(x_test)

print(confusion_matrix(y_test, y_pred))
print(model2.score(x_test, y_test))
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()


