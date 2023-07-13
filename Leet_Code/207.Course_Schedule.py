class Solution:
	def canFinish(numCourses: int, prerequisites: list) -> bool:
		adj = [[] for _ in range(numCourses)]
		indegree = [0] * numCourses
		ans = []
		
		print (numCourses, indegree)

		for pair in prerequisites:
			course = pair[0]
			prerequisite = pair[1]
			adj[prerequisite].append(course)
			indegree[course] += 1
	
def main():
	numCourses = 2
	prerequisites = [[1,0]]
	result = 0
	result = Solution.canFinish(numCourses, prerequisites)

main()