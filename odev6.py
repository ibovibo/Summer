class hayvan:

    def __init__(self, isim, yas):

        self.i=isim
        self.y=yas
        
    def ses_cikar(self):
        pass

    
class kedi (hayvan):

    def __init__(self, isim, yas):
        super().__init__(isim, yas)
    
    
    def ses_cikar(self):

        print("miyav")

    def tirmala(self):

        print("tirmalandi")



class kopek(hayvan):

    def __init__(self, isim, yas):
        super().__init__(isim, yas)
    
    def ses_cikar(self):

        print("hav")

    def getir(self):

        print("getirildi")


a1 = kedi("tekir",8)
a1.ses_cikar()
a1.tirmala()

a2 = kopek("karabas", 3)
a2.ses_cikar()
a2.getir()
