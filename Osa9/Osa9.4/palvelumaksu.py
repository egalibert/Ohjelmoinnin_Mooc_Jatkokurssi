# TEE RATKAISUSI TÄHÄN:

class Pankkitili:
	def __init__ (self, tilinomistajan :str, tilinumeron :str, saldo :float):
		self.__tilinomitaja = tilinomistajan
		self.__tilinumero = tilinumeron
		self.__saldo = saldo

	def __palvelumaksu (self):
		self.__saldo -= self.saldo / 100

	def talleta (self, maara :float):
		if (maara > 0):
			self.__saldo += maara
			self.__palvelumaksu()
		
	def nosta (self, maara :float):
		if (self.__saldo > maara):
			self.__saldo -= maara
			self.__palvelumaksu()

	@property
	def saldo(self):
		return(self.__saldo)



if __name__ == "__main__":
	tili = Pankkitili("Raimo Rahakas", "12345-6789", 1000)
	tili.nosta(100)
	print(tili.saldo)
	tili.talleta(100)
	print(tili.saldo)