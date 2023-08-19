class Solution:
	def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
		d = {}
		for i in range(len(nums)):
			if nums[i] in d:
				if abs(d[nums[i]] - i) <= k:
					return True
			d[nums[i]] = i
		return False
	
def main():
	nums = [1,2,3,1]
	k = 3
	result = True
	
	result = Solution.containsNearbyDuplicate(nums, k)