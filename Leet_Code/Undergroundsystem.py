class UndergroundSystem:

	def __init__(self):
		self.id_list = {}
		self.averagetimes = []

	def checkIn(self, id: int, stationName: str, t: int) -> None:
		self.id_list[id] = [stationName, t]

	def checkOut(self, id: int, stationName: str, t: int) -> None:
		if id in self.id_list:
			self.averagetimes.append([self.id_list[id][0], stationName, t - self.id_list[id][1]])
			print (self.averagetimes)
		

	def getAverageTime(self, startStation: str, endStation: str) -> float:
		total = 0
		times = 0
		result = 0
		for elem in self.averagetimes:
			if (startStation in elem[0] and endStation in elem[1]):
				total += elem[2]
				times += 1
		result = total / times
		result = "{0:.5f}".format(result)
		print (result)
		return (result)


# Your UndergroundSystem object will be instantiated and called as such:
def main():
	obj = UndergroundSystem()
	obj.checkIn(1,"Leeds",3)
	obj.checkIn(2,"York",8)
	obj.checkOut(1,"York",10)
	obj.checkOut(2,"Leeds",15)
	obj.checkIn(1,"York",20)
	obj.checkIn(2,"Leeds",22)
	param_3 = obj.getAverageTime("Leeds","York")
	param_3 = obj.getAverageTime("York","Leeds")
	obj.checkOut(1,"Leeds",24)
	param_3 = obj.getAverageTime("York","Leeds")
	obj.checkOut(2,"York",38)
	param_3 = obj.getAverageTime("Leeds","York")



main()
# Input
# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

# ["UndergroundSystem","checkIn","checkIn","checkOut","checkOut","checkIn","checkIn","getAverageTime","getAverageTime","checkOut","getAverageTime","checkOut","getAverageTime"]
# [[],
# [1,"Leeds",3],
# [2,"York",8],
# [1,"York",10],
# [2,"Leeds",15],
# [1,"York",20],
# [2,"Leeds",22],
# ["Leeds","York"],
# ["York","Leeds"],
# [1,"Leeds",24],
# ["York","Leeds"],
# [2,"York",38],
# ["Leeds","York"]]