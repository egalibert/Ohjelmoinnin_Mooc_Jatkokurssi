from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		
class Solution:
	def maxLevelSum(root) -> int:
		if root is None:
			return 0

		queue = deque()
		queue.append(root)
		level = 1
		max_level = 1
		max_sum = float('-inf')

		while queue:
			print(queue)
			level_sum = 0
			level_size = len(queue)

			for _ in range(level_size):
				node = queue.popleft()
				level_sum += node.val

				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			if level_sum > max_sum:
				max_sum = level_sum
				max_level = level

			level += 1

		return max_level

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

# Calculate the smallest level with the maximal sum
result = Solution.maxLevelSum(root)
print(result)  # Output: 2