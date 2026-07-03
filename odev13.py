import pandas as pd

ogreenci = {

"isim" : ["Ahmet", "Mehmet", "Cavid", "Nehir", "Azra"],

"not" : [82, 45, 37, 63, 92],

"yas" : [17, 18, 16, 17, 17]
}


df = pd.DataFrame(ogreenci)

print(df.head())
df.info()
print(df.describe())
print(df)
