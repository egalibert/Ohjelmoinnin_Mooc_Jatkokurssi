# Tee ratkaisusi tähän:

class Henkilo:

	def __init__(self, nimi :str):
		self.nimi = nimi

	def anna_etunimi(self):
		nimet = self.nimi.split()
		return (nimet[0])
	
	def anna_sukunimi(self):
		nimet = self.nimi.split()
		return (nimet[1])



if __name__ == "__main__":
	pekka = Henkilo("Pekka Python")
	print(pekka.anna_etunimi())
	print(pekka.anna_sukunimi())

	pauli = Henkilo("Pauli Pythonen")
	print(pauli.anna_etunimi())
	print(pauli.anna_sukunimi())


