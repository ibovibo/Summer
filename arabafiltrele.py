import pandas as pd

df = pd.read_csv("car_price_prediction-selected-columns.csv")
# print(df.shape)  kac satir kac sutun
# print(df.head()) ilk 5 satir

yil_min = int(input("min yil: "))
yil_max = int(input("max yil: "))

yil_filtre = df[(df["yil"] >= yil_min) & (df["yil"] <= yil_max)]
print(yil_filtre)