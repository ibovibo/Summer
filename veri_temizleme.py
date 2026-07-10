import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("google_playstore.csv")

df.drop(columns = ["App", "Size", "Type", "Price", "Content Rating" ,"Genres" ,"Last Updated", "Current Ver", "Android Ver", "In-App Purchases", "Ad Supported"], inplace = True)


df["Installs"] = df["Installs"].str.replace(",", "", regex=False)
df["Installs"] = df["Installs"].str.replace("+", "", regex=False)
df["Installs"] = df["Installs"].astype(int)

df["Rating"] = df["Rating"].fillna(df["Rating"].mean())



ort = df.groupby("Category")["Rating"].mean()
ort = ort.sort_values(ascending=False)

for kategori, ortalama in ort.items():
    print(f"{kategori} kategorisinin ortalama puani: {ortalama:.2f}")



plt.figure(figsize=(12, 6))
# figsize=(12, 6) boyutunu belirliyor - birim inc, yani 12 birim genislik, 6 birim yukseklik.
# ~35 kategori oldugu icin genis bir tuval lazim, yoksa cubuklar birbirine girer.
 
plt.bar(ort.index, ort.values)
# Asil cizim burada. plt.bar(x, y) cubuk grafik ciziyor:
# ort.index  -> x ekseni, yani kategori isimleri (GAME, EDUCATION, ...)
# ort.values -> y ekseni, yani her kategorinin ortalama rating degeri
# Her kategori icin bir cubuk ciziyor, cubugun yuksekligi o kategorinin ortalama puani kadar oluyor.
 
plt.title("Kategoriye Gore Ortalama Rating")
# Grafigin en ustune baslik yaziyor, sadece etiket amacli.
 
plt.xlabel("Kategori")
plt.ylabel("Ortalama Puan")
# X ekseninin altina "Kategori", Y ekseninin yanina "Ortalama Puan" yaziyor
# - grafigi okuyan kisi hangi eksenin ne oldugunu anlasin diye.
 
plt.xticks(rotation=90)
#rotation=90 bu isimleri dikey (90 derece dondurerek) yazdiriyor
 
plt.tight_layout()
# Kozmetik bir duzeltme Bu satir her seyi otomatik ayarlayip kenarlara sigdiriyor 

plt.show()


toplam_indirilme = df.groupby("Category")["Installs"].sum()
toplam_indirilme = toplam_indirilme.sort_values(ascending=False)

for kategori, indirme in toplam_indirilme.items():
    print(f"{kategori} kategorisinin toplam indirilmesi : {indirme}")




df["Yorum_Oranı"] = df["Reviews"] / df["Installs"]

xqc = df.groupby("Category")["Yorum_Oranı"].mean()
xqc = xqc.sort_values(ascending=False)

for kategori, oran in xqc.items():
    print(f"{kategori} kategorisinin yorum oranı : {oran:.3f}")





# .items() bir Series (senin durumunda ort veya toplam_indirilme) üzerinde gezerken,
# her turda hem index'i (kategori adı) hem de değeri (ortalama/toplam) aynı anda almanı sağlıyor.