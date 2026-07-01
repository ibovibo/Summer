
def asal_mi(n):

    for bolen in range(2, n):
        if n % bolen == 0:
            return False
    return True
    
asallar = [n for n in range(2, 101) if asal_mi(n)]
print(asallar) 



def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for i in range(20):
    print(next(gen))



liste=[[1,2],[3,4],[5,6]]

sonuc=[ sayi for alt_liste in liste for sayi in alt_liste]

print(sonuc)