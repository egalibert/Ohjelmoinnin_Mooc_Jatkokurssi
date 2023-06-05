class Solution:
	def findCircleNum(isConnected :list):
		n = len(isConnected)
		numProvinces = 0
		visited = set()

		def dfs(kauupunki):
			visited.add(kauupunki)

			for vieressa in range(n):
				if isConnected[kauupunki][vieressa] == 1 and vieressa not in visited:
					dfs(vieressa)

		for kauupunki in range(n):
			if kauupunki not in visited:
				dfs(kauupunki)
				numProvinces += 1

		return numProvinces
			

				

def main():
	result = 0
	# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
	# isConnected = [[1,0,0],[0,1,0],[0,0,1]]
	isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
	result = Solution.findCircleNum(isConnected)
	print (result)

main()
