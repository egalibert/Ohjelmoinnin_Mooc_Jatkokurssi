# TEE RATKAISUSI TÄHÄN:

class Lahja:

	def __init__(self, nimi :str, paino :int):
		self.nimi = nimi
		self.paino = paino

	def __str__(self):
		return (f"{self.nimi} ({self.paino})")

class Pakkaus:

	def __init__(self):
		self.lahjat = []

	def __str__(self):
		pass

	def lisaa_lahja(self, lahja :"Lahja"):
		self.lahjat.append(lahja)

	def yhteispaino(self):
		total = 0
		for gift in self.lahjat:
			total += gift.paino
		return (total)



if __name__ == "__main__":
	# kirja = Lahja("Aapiskukko", 2)

	# print("Lahjan nimi:", kirja.nimi)
	# print("Lahjan paino:" ,kirja.paino)
	# print("Lahja:", kirja)
	kirja = Lahja("Aapiskukko", 2)

	pakkaus = Pakkaus()
	pakkaus.lisaa_lahja(kirja)
	print(pakkaus.yhteispaino())

	cd_levy = Lahja("Pink Floyd: Dark side of the moon", 1)
	pakkaus.lisaa_lahja(cd_levy)
	print(pakkaus.yhteispaino())