# Tee ratkaisusi tähän:

class Sarja:
	def __init__(self, nimi :str, kaudet :int, genret :list):
		self.nimi = nimi
		self.kaudet = kaudet
		self.genret = genret
		self.maara = 0
		self.arvostelut = 0
		self.arvostelu = 0
	
	def arvostele(self, arvosana: int):
		self.maara += 1
		self.arvostelut += arvosana
		if (self.arvostelut > 0):
			self.arvostelu = self.arvostelut / self.maara
		else:
			self.arvostelu = 0


	def __str__(self) -> str:
		lista = self.genret
		merkkijono = ", ".join(lista)
		if (self.arvostelu == 0):
			return (f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {merkkijono}\nei arvosteluja")
		else:
			return (f"{self.nimi} ({self.kaudet} esityskautta)\ngenret: {merkkijono}\narvosteluja {self.maara}, keskiarvo {round(self.arvostelu, 1)} pistettä")



def arvosana_vahintaan(minimi :float, sarjat :list):
	uusi_lista = []
	for i in sarjat:
		if (i.arvostelu >= minimi):
			uusi_lista.append(i)
	return (uusi_lista)

def sisaltaa_genren(genre :str, sarjat :list):
	uusi_lista = []
	for sarja in sarjat:
		for i in sarja.genret:
			if (genre == i):
				uusi_lista.append(sarja)
	return (uusi_lista)


if __name__ == "__main__":
	s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	s1.arvostele(5)

	s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
	s2.arvostele(3)

	s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
	s3.arvostele(2)

	sarjat = [s1, s2, s3]

	print("arvosana vähintään 4.5:")
	for sarja in arvosana_vahintaan(4.5, sarjat):
		print(sarja.nimi)

	print("genre Comedy:")
	for sarja in sisaltaa_genren("Comedy", sarjat):
		print(sarja.nimi)