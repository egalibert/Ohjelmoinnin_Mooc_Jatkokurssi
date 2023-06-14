class Solution:
	def isFascinating(n: int) -> bool:
		num_str = ""
		num_str += str(n)
		num_str += str(n * 2)
		# print (n, num_str)
		num_str += str(n * 3)
		# print (n, num_str)
		i = 0
		total = 0
		new_list = []

		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		print (f" original string is{num_str} list is {numbers}")
		while len(num_str) > i:
			if (num_str[i] not in numbers):
				return False
			if num_str[i] in numbers:
				total += 1
				i += 1
				new_list.append(num_str[i])
		print(total)
		if total != 9:
			return False
		return True
    
def main():
	n = 192
	n1 = 100
	n2 = 783
	n3 = 111
	result = False
	result = Solution.isFascinating(n)
	print(result)
	result = Solution.isFascinating(n1)
	print(result)
	result = Solution.isFascinating(n2)
	print(result)
	result = Solution.isFascinating(n3)
	print(result)
	
	
main()