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
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		print (f" original string is{num_str} list is {numbers}")
		while (len(numbers) > i):
			if  numbers[i] not in num_str:
				return False
			if numbers[i] in num_str:
				print (numbers[i])
				# numbers.remove(numbers[i])
				total += 1
				i += 1
			print (numbers)
			# i += 1
		print (total)
		if total != 9:
			return False
		return True
    
def main():
    # n = 192
    # n = 100
    n = 783
    result = False
    result = Solution.isFascinating(n)
    print(result)
    
main()