# TEE RATKAISUSI TÄHÄN:

class ListaApuri:
	def __init__ (self):
		pass

	@classmethod
	def suurin_frekvenssi(cls, lista :list):
		eniten = 0
		luku = ""
		for i in lista:
			lkm = lista.count(i)
			if (lkm > eniten):
				luku = i
				eniten = lista.count(i)
				print(f"eniten on = {eniten}")
				print(f"luku on = {luku}")
		return (luku)

	@classmethod
	def tuplia(cls, lista :list):
		uusi_lista = []
		tuplia = 0
		for i in lista:
			lkm = 0
			if (i not in uusi_lista):
				lkm = lista.count(i)
				if (lkm > 1):
					tuplia += 1
			uusi_lista.append(i)
		return (tuplia)



if __name__ == "__main__":
	luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
	print(ListaApuri.suurin_frekvenssi(luvut))
	print(ListaApuri.tuplia(luvut))