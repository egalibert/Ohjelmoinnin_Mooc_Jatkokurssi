class Solution:
	def countNegatives(grid :list) -> int:
		total = 0
		for lista in grid:
			for number in lista:
				if number < 0:
					total += 1
		return total



def main():
	result = 0
	grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
	result = Solution.countNegatives(grid)
	print(result)

main()