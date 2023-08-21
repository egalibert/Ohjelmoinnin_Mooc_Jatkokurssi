# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution:
	def maxDepth(root) -> int:
		def dfs(root, depth):
			if not root:
				return depth
			return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
		return dfs(root, 0)

	
def main():
	root = [3,9,20,None,None,15,7]
	
	result = 0
	result = Solution.maxDepth(root)