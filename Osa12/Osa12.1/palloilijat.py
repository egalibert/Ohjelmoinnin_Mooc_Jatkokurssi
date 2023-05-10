class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __str__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, '
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')

# TEE RATKAISUSI TÄHÄN:

def eniten_maaleja(joukkue :list):
    tulos = max(joukkue, key=lambda pelaaja: pelaaja.maalit)
    return tulos.nimi

def eniten_pisteita(joukkue :list):
    tulos = max(joukkue, key=lambda pelaaja: pelaaja.maalit + pelaaja.syotot)
    return (tulos.nimi, tulos.pelinumero)

def vahiten_minuutteja(joukkue :list):
    return min(joukkue, key=lambda pelaaja: pelaaja.minuutit)



if __name__ == "__main__":
    if __name__ == "__main__":
        pelaaja1 = Palloilija("Kelju Kojootti", 13, 5, 12, 46)
        pelaaja2 = Palloilija("Maantiekiitäjä", 7, 2, 26, 55)
        pelaaja3 = Palloilija("Uka Naakka", 9, 1, 32, 26)
        pelaaja4 = Palloilija("Pelle Peloton", 12, 1, 11, 41)
        pelaaja5 = Palloilija("Hessu Hopo", 4, 3, 9, 12)

        joukkue = [pelaaja1, pelaaja2, pelaaja3, pelaaja4, pelaaja5]
        print(eniten_maaleja(joukkue))
        print(eniten_pisteita(joukkue))
        print(vahiten_minuutteja(joukkue))