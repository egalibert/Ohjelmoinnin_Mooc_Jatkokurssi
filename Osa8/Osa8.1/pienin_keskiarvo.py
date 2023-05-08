# tee ratkaisu tänne

def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
	h1 = 0
	h2 = 0
	h3 = 0

	summa = 0

	for arvo in henkilo1.keys():
		if arvo != "nimi":
			summa += henkilo1[arvo]
	h1 = summa / (len(henkilo1) - 1)

	summa = 0

	for arvo in henkilo2.keys():
			if arvo != "nimi":
				summa += henkilo2[arvo]
	h2 = summa / (len(henkilo2) - 1)

	summa = 0

	for arvo in henkilo3.keys():
			if arvo != "nimi":
				summa += henkilo3[arvo]
	h3 = summa / (len(henkilo3) - 1)

	# print(h1, h2, h3)
	if (h1 < h2 and h1 < h3):
		return(henkilo1)
	elif (h2 < h1 and h2 < h1):
		return (henkilo2)
	else:
		return (henkilo3)


if __name__ == "__main__":
	henkilo1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
	henkilo2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
	henkilo3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

	print(pienin_keskiarvo(henkilo1, henkilo2, henkilo3))