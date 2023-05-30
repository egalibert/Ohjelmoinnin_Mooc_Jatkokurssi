class MyHashSet:

	def __init__(self):
		self.list = []
		print(f"{self.list}")
		

	def add(self, key: int) -> None:
		if (key not in self.list):
			self.list.append(key)
		print(f"{self.list}")
		

	def remove(self, key: int) -> None:
		if (key in self.list):
			self.list.remove(key)
		print(f"{self.list}")
		

	def contains(self, key: int) -> bool:
		print(f"{self.list}")
		if (key in self.list):
			print(True)
			return True
		else:
			print(False)
			return False


def main ():
	myHashSet = MyHashSet()
	myHashSet.add(1);      
	myHashSet.add(2);      
	myHashSet.contains(1); 
	myHashSet.contains(3); 
	myHashSet.add(2);      
	myHashSet.contains(2); 
	myHashSet.remove(2);   
	myHashSet.contains(2); 

main()