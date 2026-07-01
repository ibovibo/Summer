class DosyaYazici:

    def __init__(self , dosya_adi):
        self
        self.d = dosya_adi



    def __enter__(self):

        self.f = open(self.d, "w")
        return self.f

    def __exit__(self, exc_type, exc, tb):

        self.f.close()
        
            

with DosyaYazici("test.txt") as f:
    f.write("merhaba")
            
        
