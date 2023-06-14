# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def getMinimumDifference(self, root) -> int:
		new_list = []
		current_list = root
		prev = None
		min_diff = float('inf')

		while current_list or new_list:
			while current_list:
				new_list.append(current_list)
				current_list = current_list.left
			current_list = new_list.pop()

			if prev is not None:
				min_diff = min(min_diff, current_list.val - prev.val)

			prev = current_list
			current_list = current_list.right

		return (min_diff)
	
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

result = Solution.getMinimumDifference(root)
print(result)




		# minimum = 10
		# new_list = sorted(root)
		# length = len(new_list)
		# for i in range (length):
		# 	for j in range(1, length):
		# 		if (new_list[j] - new_list[i] < minimum and new_list[j] - new_list[i] > 0):
		# 			minimum = new_list[j] - new_list[i]
		# return (minimum)