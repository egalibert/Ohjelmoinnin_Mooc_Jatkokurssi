class Solution:
	def checkStraightLine(coordinates: list):
		n = len(coordinates)
		if len(coordinates) < 2:
			return True 
		# index = 0
		# index2 = 1
		# index3 = 0
		difference1 = coordinates[1][0] - coordinates[0][0]
		difference2 = coordinates[1][1] - coordinates[0][1]
		print(difference1, difference2)
		# for i in range (2, len(coordinates)):
		# 	if coordinates[i][0] - coordinates[i - 1][0] != difference1 or coordinates[i][1] - coordinates[i -1 ][1] != difference2:
		# 		return False
		for i in range(2, len(coordinates)):
			x_difference = coordinates[i][0] - coordinates[i - 1][0]
			y_difference = coordinates[i][1] - coordinates[i - 1][1]

			print(f"{x_difference, y_difference}")
			

			if x_difference != difference1 or y_difference != difference2:
				return False

		return (True)
	

def main():
	result = False
	# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
	# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
	# coordinates = [[1,2],[2,3],[3,5]]
	coordinates = [[0,0],[0,1],[0,-1]]
	result = Solution.checkStraightLine(coordinates)

	print (result)

main()