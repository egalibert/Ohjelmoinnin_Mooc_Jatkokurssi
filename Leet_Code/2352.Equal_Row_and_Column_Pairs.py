class Solution:
	def equalPairs(grid :list) -> int:
		n = len(grid)
		count = 0

		for i in range(n):
			for j in range(n):
				if grid[i] == [row[j] for row in grid]:
					count += 1

		return count

def main():
	grid = [[3,2,1],[1,7,6],[2,7,7]]
	result = 0
	result = Solution.equalPairs(grid)

	print(result)

main()