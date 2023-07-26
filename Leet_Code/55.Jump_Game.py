# You are given an integer array nums. You are initially positioned at the array's 
# first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
	def canJump( nums: list) -> bool:
		i = 1
		prev = nums[0]
		if len(nums) == 1:
			return True
		if prev == 0:
			return False
		while i < len(nums) -1:
			print(prev)
			prev = max(prev -1, nums[i])
			if not prev:
				return False
			i += 1
		return True
			

def main():
	nums = [2,3,1,1,4]
	result = False
	
	result = Solution.canJump(nums)
	print (result)

main()