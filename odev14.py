import pandas as pd

ogreenci = {

"isim" : ["Ahmet", "Mehmet", "Cavid", "Nehir", "Azra", "Gül"],

"not" : [82, 45, 37, 63, 92, None],

"yas" : [17, 18, 16, 17, 17, 18]
}


df = pd.DataFrame(ogreenci)

df["not"] = df["not"].fillna(100)

df["gecti_mi"] = df["not"] >= 50
print(df[["isim", "gecti_mi"]])


gecen = df[df["not"] > 50]


gecen_sirali = gecen.sort_values("not")


ort = df.groupby("yas")["not"].mean()
