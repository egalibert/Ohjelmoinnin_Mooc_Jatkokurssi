# Tee tehtävän 1 ratkaisu tänne

class Orkesteri:
	def __init__(self):
		self.__muusikot = []
		self.__soittokerrat = 0

	def lisaa_muusikko(self, muusikko: "Muusikko"):
		self.__muusikot.append(muusikko)

	def __str__(self):
		yhteistaso = 0
		kuvaus = ""

		kuvaus += f"Orkesteri (soittokertoja {self.__soittokerrat}, jäsenten kokemuksen keskiarvo:"

		for i in self.__muusikot:
			yhteistaso += int(i.kokemus())
		kuvaus += f" {yhteistaso / len(self.__muusikot):.1f})"

		for i in self.__muusikot:
			kuvaus += f"\n{i.__str__()}"
		
		return (kuvaus)
	
	def soita(self):
		self.__soittokerrat += 1
		for i in self.__muusikot:
			i.soita()


class Muusikko:
	def __init__(self, nimi :str, soitin :str):
		self.__nimi = nimi
		self.__soitin = soitin
		self.__taso = 0
		
	def	__str__(self):
		return f"{self.__nimi}, soitin: {self.__soitin}. Kokemus: {self.__taso}"
	
	def kokemus(self):
		return f"{self.__taso}"
	
	def soita(self):
		self.__taso += 1
	

# matti = Muusikko("Matti", "Tuuba")
# print(matti)
# print(matti.kokemus())

# matti.soita()
# print(matti.kokemus())
# print(matti)

# matti.soita()
# matti.soita()
# matti.soita()
# matti.soita()
# print(matti)
matti = Muusikko("Matti", "Tuuba")
teppo = Muusikko("Teppo", "Banjo")

orkesteri = Orkesteri()
orkesteri.lisaa_muusikko(matti)
orkesteri.lisaa_muusikko(teppo)

print(orkesteri)

orkesteri.soita()

print()
print(orkesteri)

matti.soita()

print()
print(orkesteri)

madonna = Muusikko("Madonna", "Piano")
orkesteri.lisaa_muusikko(madonna)
orkesteri.soita()

print()
print(orkesteri)
