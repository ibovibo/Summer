import json
from odev3 import hata_yakala

class Gorev:

    def __init__(self,id,baslik,tamamlandi,tarih):
        self.i=id
        self.b=baslik
        self.t=tamamlandi
        self.tarih=tarih
    
    def __str__(self):
        return f"[{self.i}] {self.b} - {self.tarih} - Tamamlandi: {self.t}"

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





class AcilGorev (Gorev):

    def __init__(self,id,baslik,tamamlandi,tarih,oncelik_puani):
        super().__init__(id,baslik,tamamlandi,tarih)
        self.o = oncelik_puani

    def oncelik(self):
        
        if self.o == 1:
            return "onemsiz"

        elif  2 <= self.o <= 4:
            return "halledilmeli"
        
        elif self.o == 5:

            return "acil"
        
        else:
            raise ValueError 
    

class NormalGorev (Gorev):
    pass

        

class GorevListesi:

    def __init__(self):
        self.gorevler = []
        self.i = 0
    
    def gorev_ekle(self, gorev):
        self.gorevler.append(gorev)

    
    def __iter__(self):
        return self

    
    def __next__(self):

        if self.i == len(self.gorevler):
           raise StopIteration

        else:

            gorev = self.gorevler[self.i]
            self.i += 1
            return gorev
        



liste = GorevListesi()
liste.gorev_ekle(AcilGorev(1, "odevi bitir", False, "2026-07-01", 5))
liste.gorev_ekle(NormalGorev(2, "kitap oku", False, "2026-07-02"))

for g in liste:
    print(g)
    


