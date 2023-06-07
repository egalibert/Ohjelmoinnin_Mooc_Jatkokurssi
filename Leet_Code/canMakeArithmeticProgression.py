class Solution:
	def canMakeArithmeticProgression(arr: list):
		neg_index = 0
		pos_index = arr[1] - arr[0]
		neg_index = pos_index * -1

		previous = 0
		difference = (pos_index - neg_index) / (len(arr)- 1)
		print (pos_index, neg_index, difference)

		for i in range(len(arr) - 1):
			expected = neg_index + i * difference
			if expected not in arr:
				return False
def main():
	result = False
	# arr = [3,5,1]
	# arr = [1,2,4]
	# arr = [1,10,10,10,19]
	arr = [1,5,6,10]
	# arr = [0,0,0,0]
	result = Solution.canMakeArithmeticProgression(arr)
	print (result)

main()