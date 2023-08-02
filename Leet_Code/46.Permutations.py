class Solution:
	def permute(self, nums: list[int]) -> list[list[int]]:
		def backtrack(nums, path): 
			if not nums: 
				result.append(path) 
				return 
			for i in range(len(nums)): 
				backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) 
		result = [] 
		backtrack(nums, []) 
		return result 
	
def main():
	nums = [1,2,3]
	result = []
	result = Solution.permute(nums)

	print (result)