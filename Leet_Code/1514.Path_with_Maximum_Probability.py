from collections import deque

class Solution:
	def maxProbability(n: int, edges: list, succProb: list, start: int, end: int) -> float:
		adj = [[] for _ in range(n)]
		for i in range(len(edges)):
			u, v = edges[i]
			p = succProb[i]
			adj[u].append((v, p))
			adj[v].append((u, p))

		print (adj)

		dist = [0.0] * n
		dist[start] = 1.0

		queue = deque([start])

		while queue:
			curr = queue.popleft()

			for node, prob in adj[curr]:
				new_prob = dist[curr] * prob

				if new_prob > dist[node]:
					dist[node] = new_prob
					queue.append(node)

		return dist[end]
	
def main():
	n = 3
	edges = [[0,1],[1,2],[0,2]]
	succProb = [0.5,0.5,0.2]
	start = 0
	end = 2
	
	result = 0

	result = Solution.maxProbability(n, edges, succProb, start, end)
	print (result)
	
main()