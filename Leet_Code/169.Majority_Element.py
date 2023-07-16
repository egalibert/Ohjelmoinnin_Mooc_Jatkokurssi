class Solution:
	def majorityElement(nums: list) -> int:
		most = 0
		total = 0
		for number in nums:
			if (nums.count(number) > total):
				most = number
				total = (nums.count(number))

		return (most)

	
def main():
	# nums = [3,2,3]
	nums = [2,2,1,1,1,2,2]
	result = 0
	result = Solution.majorityElement(nums)
	print (result)
	
main()


# class Solution:
#     def majorityElement(self, nums: list) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n//2]