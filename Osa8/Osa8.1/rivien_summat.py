# tee ratkaisu tänne

def rivien_summat(matriisi: list):
	for rivi in matriisi:
		summa = 0
		for arvo in rivi:
			summa += arvo
			print(arvo)
		rivi.append(summa)
		print(rivi)

if __name__ == "__main__":
	matriisi = [[1, 2], [3, 4]]
	rivien_summat(matriisi)
	print(matriisi)