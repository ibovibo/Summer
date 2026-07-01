import json
from odev3 import hata_yakala

class gorev:

    def __init__(self,id,baslik,tamamlandi,tarih):
        self.i=id
        self.b=baslik
        self.t=tamamlandi
        self.tarih=tarih


@hata_yakala
def gorev_ekle(id,baslik,tarih):
    
    
    
    try: 
        with open("gorevler.json", "r") as d:
            veri=json.load(d)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
        veri={}
    
    yeni=gorev(id, baslik, False, tarih)
    veri[id]=yeni.__dict__

    with open("gorevler.json", "w") as d:
        json.dump(veri, d)
        print(veri[id])

@hata_yakala
def gorev_sil(id):
        
    with open("gorevler.json", "r") as d:
        veri=json.load(d)
        del veri[id]

    with open("gorevler.json", "w") as d:
        json.dump(veri, d)

@hata_yakala
def tamamlandi_isle(id):
        
    with open("gorevler.json", "r") as d:
        veri=json.load(d)
        veri[str(id)]["t"] = True

    with open("gorevler.json", "w") as d:
        json.dump(veri, d)

@hata_yakala
def listele():
        
    with open("gorevler.json", "r") as d:
        veri=json.load(d)
        
        for id, gorev in veri.items():
            print(id,gorev)


gorev_ekle(1, "odevi bitir", "2026-06-28")
gorev_ekle(2, "kitap oku", "2026-06-29")
listele()



        
    


