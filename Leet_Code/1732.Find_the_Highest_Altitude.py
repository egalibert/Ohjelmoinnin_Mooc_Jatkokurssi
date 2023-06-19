class Solution:
	def largestAltitude(gain :list) -> int:
		current = 0
		largest = 0
		for i in gain:
			current += i

			if current > largest:
				largest = current
		return (largest)

def main ():
	gain = [-5,1,5,0,-7]
	# gain = [-4,-3,-2,-1,4,3,2]
	result = 0 
	result = Solution.largestAltitude(gain)

	print(result)

main()
