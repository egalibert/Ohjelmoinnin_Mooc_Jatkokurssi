# Tee tehtävän 2 ratkaisu tänne

from random import *

def arvo(lista :list):

	uusi_lista = []

	if len(lista) == len(uusi_lista):
		raise StopIteration

	while len(uusi_lista) < (len(lista)):
		arpanumero :int = randint(0, (len(lista) - 1))

		if lista[arpanumero] not in uusi_lista:
			yield lista[arpanumero]
			uusi_lista.append(lista[arpanumero])
		if len(lista) == len(uusi_lista):
			raise StopIteration
		else:
			continue



# arpoja = arvo(['Kana', 'Karhu', 'Gorilla', 'Kettu'])
# for i in range(5):
# 	print(next(arpoja))