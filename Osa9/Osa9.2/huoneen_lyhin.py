# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return self.nimi

class Huone:
    def __init__(self):
        self.henkilot = []

    def lisaa(self, henkilo: "Henkilo"):
        self.henkilot.append(henkilo)

    def on_tyhja(self):
        if (len(self.henkilot) > 0):
            return False
        else:
            return (True)

    def tulosta_tiedot(self):
        yhteispituus = 0
        for h in self.henkilot:
            yhteispituus += h.pituus

        print(f"Huoneessa {len(self.henkilot)} henkilöä, yhteispituus {yhteispituus} cm")
        for person in self.henkilot:
            print(f"{person.nimi} ({person.pituus})")

    def lyhin(self):
        lyhyin = 300
        person = ""
        if (len(self.henkilot) > 0):
            for h in self.henkilot:
                if (h.pituus < lyhyin):
                    lyhyin = h.pituus
                    person = h.nimi
            for i in self.henkilot:
                if (i.nimi == person):
                    return (i)
        else:
            return (None)

    def poista_lyhin(self):
        lyhyin = 300
        person = ""
        if (len(self.henkilot) > 0):
            for h in self.henkilot:
                if (h.pituus < lyhyin):
                    lyhyin = h.pituus
                    person = h.nimi
            for i in self.henkilot:
                if (i.nimi == person):
                    self.henkilot.remove(i)
                    return (i)
        else:
            return (None)




if __name__ == "__main__":
    # huone = Huone()
    # print("Huone tyhjä?", huone.on_tyhja())
    # huone.lisaa(Henkilo("Lea", 183))
    # huone.lisaa(Henkilo("Kenya", 182))
    # huone.lisaa(Henkilo("Auli", 186))
    # huone.lisaa(Henkilo("Nina", 172))
    # huone.lisaa(Henkilo("Terhi", 185))
    # print("Huone tyhjä?", huone.on_tyhja())
    # huone.tulosta_tiedot()

    # huone = Huone()

    # print("Huone tyhjä?", huone.on_tyhja())
    # print("Lyhin:", huone.lyhin())

    # huone.lisaa(Henkilo("Lea", 183))
    # huone.lisaa(Henkilo("Kenya", 182))
    # huone.lisaa(Henkilo("Nina", 172))
    # huone.lisaa(Henkilo("Auli", 186))

    # print()

    # print("Huone tyhjä?", huone.on_tyhja())
    # print("Lyhin:", huone.lyhin())

    # print()

    # huone.tulosta_tiedot()

    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()