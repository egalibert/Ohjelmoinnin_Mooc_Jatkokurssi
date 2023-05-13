# Tee tehtävän 3 ratkaisu tänne

class Laskin:
	def __init__(self):
		self.historia = 0
		with open("historia.txt", "a") as tiedosto:
			tiedosto.close()

	def toiminnot(self):
		print(f"Toiminnot:")
		print(f"0 - ohjelman lopettaminen")
		print(f"1 - laske yhteenlasku (+)")
		print(f"2 - laske vähennyslasku (-)")
		print(f"3 - laske kertolasku (*)")
		print(f"4 - laske jakolasku (/)")
		print(f"5 - näytä historia")
		print(f"6 - tyhjennä historia")
		print(f"7 - näytä toiminnot")

	def yhteenlasku(self):
		print(f"Yhteenlasku (+)")
		luku1 = float(input(f"Anna luku: "))
		luku2 = float(input(f"Anna luku: "))
		print(f"Tulos: {luku1 + luku2}")
		self.historia += 1
		with open("historia.txt", "a") as file:
			file.write(f"{luku1};+;{luku2};{luku1 + luku2}\n")

	def erotus(self):
		print(f"Vähennyslasku (-)")
		luku1 = float(input(f"Anna luku: "))
		luku2 = float(input(f"Anna luku: "))
		print(f"Tulos: {luku1 - luku2}")
		self.historia += 1
		with open("historia.txt", "a") as file:
				file.write(f"{luku1};-;{luku2};{luku1 - luku2}\n")

	def kertoma(self):
		print(f"Kertolasku (*)")
		luku1 = float(input(f"Anna luku: "))
		luku2 = float(input(f"Anna luku: "))
		print(f"Tulos: {luku1 * luku2}")
		self.historia += 1
		with open("historia.txt", "a") as file:
			file.write(f"{luku1};*;{luku2};{luku1 * luku2}\n")

	def jakolasku(self):
		print(f"Jakolasku (/)")
		luku1 = float(input(f"Anna luku: "))
		luku2 = float(input(f"Anna luku: "))
		print(f"Tulos: {luku1 / luku2}")
		self.historia += 1
		with open("historia.txt", "a") as file:
			file.write(f"{luku1};/;{luku2};{luku1 / luku2}\n")

	def nayta_historia(self):
		if (self.historia == 0):
			print(f"Historiatietoja ei saatavilla.")
		else:
			print(f"Historiassa {self.historia} tulosta:")
			with open("historia.txt", "r") as file:
				for rivi in file:
					rivi = rivi.replace("\n", "")
					osat = rivi.split(";")
					numero1 = osat[0]
					merkki = osat[1]
					numero2 = osat[2]
					tulos = osat[3]
					print(f"{numero1} {merkki} {numero2} = {tulos}")

	def tyhjenna_historia(self):
		self.historia = 0
		with open("historia.txt", "w") as file:
			pass
		print(f"Historia tyhjennetty.")

	def start(self):
		with open("historia.txt", "r")as file:
			maara = 0
			for line in file:
				maara += 1
			self.historia = maara
			print(f"Nelilaskin")
			print(f"Historiassa {self.historia} tulosta")
			self.toiminnot()
			while (True):
				valinta = int(input("Valitse toiminto: "))
				if (valinta == 0):
					print(f"Lopetetaan...")
					file.close()
					break
				elif valinta == 1:
					self.yhteenlasku()
				elif valinta == 2:
					self.erotus()
				elif valinta == 3:
					self.kertoma()
				elif valinta == 4:
					self.jakolasku()
				elif valinta == 5:
					self.nayta_historia()
				elif valinta == 6:
					self.tyhjenna_historia()
				elif valinta == 7:
					self.toiminnot()


app = Laskin()
app.start()