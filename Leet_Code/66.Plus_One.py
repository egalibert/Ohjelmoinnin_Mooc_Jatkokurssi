class Solution:
	def plusOne(self, digits: list[int]) -> list[int]:

		for i in range(len(digits)-1,-1,-1):
			if digits[i] == 9:
				digits[i] = 0 
			else:
				digits[i] += 1
				return digits
		return [1] + digits
		
	
def main():
	digits = [1,2,3]
	result = []
	result = Solution.plusOne(digits)

	print (result)
	
main()