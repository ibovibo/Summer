import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

df.drop(columns=["Cabin", "Ticket", "PassengerId"], inplace = True)


df["aile_boyutu"] = df["SibSp"] + df["Parch"] +1


df["yas_grubu"] = pd.cut(df["Age"],
                       bins = [0, 12, 25, 60, 120],
                       labels = ["cocuk", "genc", "yetiskin", "yasli"])
                        

print(df[["Name", "yas_grubu", "aile_boyutu"]])