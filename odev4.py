import json


def not_ekle(isim, puan):
    try:
        with open("ogrenci.json", "r") as f:
        
             veri = json.load(f)
    except FileNotFoundError as e:
        print(e)
        veri={}
        
    veri[isim] = puan
    with open("ogrenci.json", "w") as f:
        json.dump(veri, f)

def not_oku(isim):

    with open ("ogrenci.json", "r") as f:

        veri=json.load(f)

        print(veri[isim])

def ort_goster():

    with open ("ogrenci.json", "r") as f:
         
        puanlar=json.load(f)
        ort=sum(puanlar.values())/len(puanlar)
        print(ort)




not_ekle("Ali", 90)
not_ekle("Veli", 75)
not_ekle("Ayse", 85)
not_oku("Ali")
ort_goster()