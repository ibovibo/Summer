import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

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

y_pred = model.predict(x_test)

print(confusion_matrix(y_test, y_pred))
print(model.score(x_test, y_test))
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()

# predict     → tahminleri al
# confusion   → tahmin vs gerçek, 4 kutu
# report      → o kutulardan metrikler
# heatmap     → aynı kutuların görseli