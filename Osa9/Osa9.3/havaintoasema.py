# TEE RATKAISUSI TÄHÄN:

class Havaintoasema:
	def __init__ (self, nimi :str):
		self.__nimi = nimi
		self.__havainnot = []
		self.__maara = 0

	def lisaa_havainto(self, havainto :str):
		self.__havainnot.append(havainto)
		self.__maara += 1

	def viimeisin_havainto(self):
		i = 0
		if len(self.__havainnot) > 0:
			while (i < len(self.__havainnot) - 1):
				i += 1
			return (self.__havainnot[i])
		else:
			return ("")

	def havaintojen_maara(self):
		return (self.__maara)

	def __str__ (self):
		return f"{self.__nimi}, {self.__maara} havaintoa"



if __name__ == "__main__":
	asema = Havaintoasema("Kumpula")
	asema.lisaa_havainto("Sadetta 10mm")
	asema.lisaa_havainto("Aurinkoista")
	print(asema.viimeisin_havainto())

	asema.lisaa_havainto("Ukkosta")
	print(asema.viimeisin_havainto())

	print(asema.havaintojen_maara())
	print(asema)