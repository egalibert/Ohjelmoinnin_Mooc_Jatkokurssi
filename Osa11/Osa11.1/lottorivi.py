# TEE RATKAISUSI TÄHÄN:

class Lottorivi:
	def __init__ (self, kierros :int, rivi :list):
		self.kierros = kierros
		self.rivi = rivi
		
	def osumien_maara(self, pelattu_rivi: list):
		return len([numero for numero in pelattu_rivi if numero in self.rivi])

	def osumat_paikoillaan(self, pelattu_rivi :list):
		return [numero if numero in self.rivi else -1 for numero in pelattu_rivi]
		


if __name__ == "__main__":
	oikea = Lottorivi(8, [1,2,3,10,20,30,33])
	oma_rivi = [1,4,7,10,11,20,30]

	print(oikea.osumat_paikoillaan(oma_rivi))