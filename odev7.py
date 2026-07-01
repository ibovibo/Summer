import math

class Vektor:

    def __init__(self, degerx, degery):
        self.x = degerx
        self.y = degery


    def __add__(self,other):

        return Vektor(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        
        return int(math.sqrt(self.x**2 + self.y**2))
    
    def __str__(self):
        return(f"yeni vektor boyutu{self.x, self.y}")


v1 = Vektor(3, 4)
v2 = Vektor(1, 2)
print(v1 + v2)   
print(v1)        
print(len(v1))   
