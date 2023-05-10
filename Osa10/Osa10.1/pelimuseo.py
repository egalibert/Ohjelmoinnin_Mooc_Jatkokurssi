# TEE RATKAISUSI TÄHÄN:
class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi

class Pelivarasto:
    def __init__(self):
        self.__pelit = []

    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit


class Pelimuseo(Pelivarasto):
    def __init__ (self):
        super().__init__()

    def anna_pelit(self):
        year = 1990
        uusi_lista = []
        self.__pelit = super().anna_pelit()
        for i in self.__pelit:
            print(f"Peli on {i.nimi} vuosi on {i.vuosi}")
            if i.vuosi <= year:
                uusi_lista.append(i)
            
        return (uusi_lista)

if __name__ == "__main__":
    museo = Pelimuseo()
    museo.lisaa_peli(Tietokonepeli("IK+","System 3",1987))
    museo.lisaa_peli(Tietokonepeli("Final Fantasy VII","Square",1997))
    museo.lisaa_peli(Tietokonepeli("Sim City 2000","Maxis",1993))
    museo.lisaa_peli(Tietokonepeli("Doom","ID Software",1993))
    museo.lisaa_peli(Tietokonepeli("Great Giana Sisters","Rainbow Arts",1987))
    museo.lisaa_peli(Tietokonepeli("Pool of Radiance","SSI",1988))
    for peli in museo.anna_pelit():
        print(peli.nimi)


    # Tietokonepeli("IK+","System 3",1987),
    #  Tietokonepeli("Sim City 2000","Maxis",1993),
    #   Tietokonepeli("Doom","ID Software",1993),
    #    Tietokonepeli("Pool of Radiance","SSI",1988),
    #     Tietokonepeli("Great Giana Sisters","Rainbow Arts",1987),
    #      Tietokonepeli("Final Fantasy VII","Square",1997)