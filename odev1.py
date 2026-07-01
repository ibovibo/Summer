class BankaHesabi:

    def __init__(self, isim, bakiye):
        self.b= bakiye
        self.i= isim

    def para_yatir(self, miktar):

        self.b+= miktar
    
    def para_cek(self, miktar):
                       
        if miktar > self.b:
            raise ValueError("Yetersiz bakiye")
            
        else:         
            self.b-= miktar
           
    
    def __str__(self):
        return f"{self.i} - Bakiye: {self.b} tl"
        
hesap = BankaHesabi(input("İsim: "), int(input("Bakiye: ")))

try:
 hesap.para_cek(int(input("Çekilecek miktar: ")))
except ValueError as e:
 print(e)

hesap.para_yatir(int(input("Yatirilacak miktar: ")))

print(hesap)



