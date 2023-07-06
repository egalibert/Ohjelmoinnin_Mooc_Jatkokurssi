class Solution:
	def minSubArrayLen(target: int, nums: list[int]) -> int:
		total = 0
		i = 0
		ans = len(nums)

		if sum(nums) < target: 
			return 0 
		
		for r , val in enumerate(nums):
			total  += val
			while total >= target:
				total -= nums[i]
				ans = min(ans, r - i + 1)
				i += 1

		return ans  
	
def main():
	# target = 7

	# nums = [2,3,1,2,4,3]
	# nums = [1,4,4]
	target = 213
	nums = [12,28,83,4,25,26,25,2,25,25,25,12]
	result = 0
	result = Solution.minSubArrayLen(target, nums)
	
	print (result)

main()