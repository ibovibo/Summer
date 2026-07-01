import time

def sure_olc(fonksiyon):
    
    
    def sarmalayici():
        baslangic=time.time()
        fonksiyon()
        bitis=time.time()
        print(f"sure = {bitis - baslangic}")
    return sarmalayici


def tekrar(n):

    def decorator(fonksiyon):   
        def sarmalayici():
            for i in range(n):
                fonksiyon()
        return sarmalayici
    return decorator



def hata_yakala(fonksiyon):   
    def sarmalayici(*args, **kwargs):
        try:
            fonksiyon(*args, **kwargs)
        except Exception as e:
            print(f"Hata: {e}")
    return sarmalayici

        
        
     



  