# TEE RATKAISUSI TÄHÄN:

def suodata_kielletyt(merkkijono: str, kielletyt: str):
	testi = [kirjain for kirjain in merkkijono if kirjain not in kielletyt]
	return "".join(testi)


if __name__ == "__main__":
	lause = "Suo! kuokka, ja python: hieno yhdistelmä!??!?!"
	suodatettu = suodata_kielletyt(lause, "!?:,.")
	print(suodatettu)