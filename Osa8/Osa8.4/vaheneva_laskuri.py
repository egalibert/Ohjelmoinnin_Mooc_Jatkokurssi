# Tee ratkaisusi tähän:
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa
        self.original = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        if (self.arvo > 0):
            self.arvo -= 1

    # ja tänne muut metodit

    def nollaa(self):
        self.arvo = 0

    def palauta_alkuperainen_arvo(self):
        self.arvo = self.original
  

if __name__ == "__main__":
    # laskuri = VahenevaLaskuri(10)
    # laskuri.tulosta_arvo()
    # laskuri.vahenna()
    # laskuri.tulosta_arvo()
    # laskuri.vahenna()
    # laskuri.tulosta_arvo()
    # laskuri = VahenevaLaskuri(2)
    # laskuri.tulosta_arvo()
    # laskuri.vahenna()
    # laskuri.tulosta_arvo()
    # laskuri.vahenna()
    # laskuri.tulosta_arvo()
    # laskuri.vahenna()
    # laskuri.tulosta_arvo()
    # laskuri = VahenevaLaskuri(100)
    # laskuri.tulosta_arvo()
    # laskuri.nollaa()
    # laskuri.tulosta_arvo()
    laskuri = VahenevaLaskuri(55)
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.vahenna()
    laskuri.tulosta_arvo()
    laskuri.palauta_alkuperainen_arvo()
    laskuri.tulosta_arvo()