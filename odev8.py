class sebzeler:

    def __init__(self):
        self.sebze = ["patates", "biber", "patlican"]
        self.i = 0

    
    def __iter__(self):
        return self

    
    def __next__(self):

        if self.i == len(self.sebze):
           raise StopIteration

        else:

            sebze = self.sebze[self.i]
            self.i += 1
            return sebze
        

# self.i = 0 → self.sebze[0] = "patates" → return "patates" → self.i = 1
# self.i = 1 → self.sebze[1] = "biber"   → return "biber"   → self.i = 2
# self.i = 2 → self.sebze[2] = "patlican"→ return "patlican"→ self.i = 3
# self.i = 3 → len(self.sebze) == 3      → StopIteration

sepet = sebzeler()
for s in sepet:
    print(s)