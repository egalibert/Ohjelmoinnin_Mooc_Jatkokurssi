# Tee ratkaisusi tähän:

class Tavara:
	def __init__ (self, nimi :str, paino :int):

		self.__nimi = nimi
		self.__paino = paino

	def nimi(self):
		return (self.__nimi)

	def paino(self):
		return (self.__paino)

	def __str__ (self):
		return f"{self.__nimi} ({self.__paino} kg)"

class Matkalaukku:
	def __init__ (self, maksimipaino :int):
		self.maksimipaino = maksimipaino
		self.tavarat = []
		self.weight = 0

	def lisaa_tavara(self, tavara :"Tavara"):
		if (self.maksimipaino - (tavara.paino() + self.weight) >= 0):
			self.tavarat.append(tavara)
			self.weight += tavara.paino()
		else:
			pass

	def tulosta_tavarat(self):
		for i in self.tavarat:
			print(i)

	def paino(self):
		return(self.weight)

	def raskain_tavara(self):
		raskain_t = None
		raskain = 0
		for i in self.tavarat:
			if (i.paino() > raskain or raskain_t == None):
				raskain = i.paino()
				raskain_t = i
		return (raskain_t)


	def __str__ (self):
		if (len(self.tavarat) != 1):
			return f"{len(self.tavarat)} tavaraa ({self.weight} kg)"
		else:
			return f"{len(self.tavarat)} tavara ({self.weight} kg)"


class Lastiruuma:
	def __init__ (self, maximum :int):
		self.maximum = maximum
		self.matkalaukut = []
		self.weight = 0
	
	def lisaa_matkalaukku(self, matkalaukku :"Matkalaukku"):
		if (self.maximum - (matkalaukku.paino() + self.weight) >= 0):
			self.matkalaukut.append(matkalaukku)
			self.weight += matkalaukku.paino()
		else:
			pass

	def __str__ (self):
		if (len(self.matkalaukut) != 1):
			return f"{len(self.matkalaukut)} matkalaukkua, tilaa {self.maximum - self.weight} kg"
		else:
			return f"{len(self.matkalaukut)} matkalaukku, tilaa {self.maximum - self.weight} kg"

	def tulosta_tavarat(self):
		for i in self.matkalaukut:
			i.tulosta_tavarat()



if __name__ == "__main__":
	# kirja = Tavara("Aapiskukko", 2)
	# puhelin = Tavara("Nokia 3210", 1)

	# print("Kirjan nimi:", kirja.nimi())
	# print("Kirjan paino:", kirja.paino())

	# print("Kirja:", kirja)
	# print("Puhelin:", puhelin)
	# kirja = Tavara("Aapiskukko", 2)
	# puhelin = Tavara("Nokia 3210", 1)
	# tiiliskivi = Tavara("Tiiliskivi", 4)

	# matkalaukku = Matkalaukku(5)
	# print(matkalaukku)

	# matkalaukku.lisaa_tavara(kirja)
	# print(matkalaukku)

	# matkalaukku.lisaa_tavara(puhelin)
	# print(matkalaukku)

	# matkalaukku.lisaa_tavara(tiiliskivi)
	# print(matkalaukku)

	# kirja = Tavara("Aapiskukko", 2)
	# puhelin = Tavara("Nokia 3210", 1)
	# tiiliskivi = Tavara("Tiiliskivi", 4)

	# matkalaukku = Matkalaukku(10)
	# matkalaukku.lisaa_tavara(kirja)
	# matkalaukku.lisaa_tavara(puhelin)
	# matkalaukku.lisaa_tavara(tiiliskivi)

	# print("Matkalaukussa on seuraavat tavarat:")
	# matkalaukku.tulosta_tavarat()
	# paino_yht = matkalaukku.paino()
	# print(f"Yhteispaino: {paino_yht} kg")

	# kirja = Tavara("Aapiskukko", 2)
	# puhelin = Tavara("Nokia 3210", 1)
	# tiiliskivi = Tavara("Tiiliskivi", 4)

	# matkalaukku = Matkalaukku(10)
	# matkalaukku.lisaa_tavara(kirja)
	# matkalaukku.lisaa_tavara(puhelin)
	# matkalaukku.lisaa_tavara(tiiliskivi)

	# raskain = matkalaukku.raskain_tavara()
	# print(f"Raskain tavara: {raskain}")

	# lastiruuma = Lastiruuma(1000)
	# print(lastiruuma)

	# kirja = Tavara("Aapiskukko", 2)
	# puhelin = Tavara("Nokia 3210", 1)
	# tiiliskivi = Tavara("Tiiliskivi", 4)

	# adan_laukku = Matkalaukku(10)
	# adan_laukku.lisaa_tavara(kirja)
	# adan_laukku.lisaa_tavara(puhelin)

	# pekan_laukku = Matkalaukku(10)
	# pekan_laukku.lisaa_tavara(tiiliskivi)

	# lastiruuma.lisaa_matkalaukku(adan_laukku)
	# print(lastiruuma)

	# lastiruuma.lisaa_matkalaukku(pekan_laukku)
	# print(lastiruuma)

	kirja = Tavara("Aapiskukko", 2)
	puhelin = Tavara("Nokia 3210", 1)
	tiiliskivi = Tavara("Tiiliskivi", 4)

	adan_laukku = Matkalaukku(10)
	adan_laukku.lisaa_tavara(kirja)
	adan_laukku.lisaa_tavara(puhelin)

	pekan_laukku = Matkalaukku(10)
	pekan_laukku.lisaa_tavara(tiiliskivi)

	lastiruuma = Lastiruuma(1000)
	lastiruuma.lisaa_matkalaukku(adan_laukku)
	lastiruuma.lisaa_matkalaukku(pekan_laukku)

	print("Ruuman matkalaukuissa on seuraavat tavarat:")
	lastiruuma.tulosta_tavarat()