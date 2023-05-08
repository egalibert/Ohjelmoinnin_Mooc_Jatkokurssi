# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.tulos = 0

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.tulos += luku

    def lukujen_maara(self):
        return(self.lukuja)
    
    def summa(self):
        return (self.tulos)

    def keskiarvo(self):
        if (self.tulos == 0):
            return (0)
        else:
            return (self.tulos / self.lukuja)


tilasto = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()
while (True):
    luku = int(input("Anna lukuja:"))
    if (luku == -1):
        print(f"Summa: {tilasto.summa()}")
        print(f"Keskiarvo: {tilasto.keskiarvo()}")
        print(f"Parillisten summa: {parilliset.summa()}")
        print(f"Parittomien summa: {parittomat.summa()}")
        break
    if (luku % 2 == 0):
        parilliset.lisaa_luku(luku)
    else:
        parittomat.lisaa_luku(luku)
    tilasto.lisaa_luku(luku)