import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

df.drop(columns=["Cabin", "Ticket", "Name", "PassengerId"], inplace = True)

df["Sex"] = df["Sex"].map({"male":0, "female":1})

df.dropna(subset=["Embarked"], inplace = True)

print(df.head())