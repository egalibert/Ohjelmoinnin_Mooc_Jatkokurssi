# TEE RATKAISUSI TÄHÄN:

class Auto:
	def __init__(self):
		self.__tankki = 0
		self.__ajettu = 0
		
	def tankkaa(self):
		self.__tankki = 60

	def aja(self, km :int):
		while (km > 0 and self.__tankki > 0):
			self.__tankki -= 1
			self.__ajettu += 1
			km -= 1

	def __str__(self):
		return f"Auto: ajettu {self.__ajettu} km, bensaa {self.__tankki} litraa"




if __name__ == "__main__":
	auto = Auto()
	print(auto)
	auto.tankkaa()
	print(auto)
	auto.aja(20)
	print(auto)
	auto.aja(50)
	print(auto)
	auto.aja(10)
	print(auto)
	auto.tankkaa()
	auto.tankkaa()
	print(auto)