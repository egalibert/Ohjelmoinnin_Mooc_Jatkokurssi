import random

class RandomizedSet:
	def __init__(self):
		self.set = []
		self.set_map = {}

	def insert(self, val: int) -> bool:
		if (val in self.set_map):
			return False
		self.set_map[val] = len(self.set)
		self.set.append(val)
		return True

	def remove(self, val: int) -> bool:
		if not val in self.set:
			return False
		last_elem = self.set[-1]
		index_to_remove = self.set_map[val]

		self.set_map[last_elem] = index_to_remove
		self.set[index_to_remove] = last_elem

		self.set[-1] = val
		self.set.pop()
		self.set_map.pop(val)
		return (True)

	def getRandom(self) -> int:
		return random.choice(self.set)

		

def main():
	randomizedSet = RandomizedSet()
	randomizedSet.insert(1); 
	randomizedSet.insert(2); 
	randomizedSet.getRandom(); 
	randomizedSet.remove(1); 
	randomizedSet.insert(2); 
	randomizedSet.getRandom(); 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()