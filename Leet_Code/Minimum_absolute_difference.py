# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def getMinimumDifference(root) -> int:
		for value in root:
			TreeNode(value)
	
def main():
	root = [4,2,6,1,3]
	
	# root = [1,0,48,12,49]
	result = 0
	result = Solution.getMinimumDifference(root)
	
	print (result)

main()




		# minimum = 10
		# new_list = sorted(root)
		# length = len(new_list)
		# for i in range (length):
		# 	for j in range(1, length):
		# 		if (new_list[j] - new_list[i] < minimum and new_list[j] - new_list[i] > 0):
		# 			minimum = new_list[j] - new_list[i]
		# return (minimum)