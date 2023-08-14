class Solution:
	def findKthLargest(nums: list[int], k: int) -> int:
		return sorted(nums) [-k]
	
def main():
	nums = [3,2,3,1,2,4,5,5,6]
	k = 4

	result  = 0
	result  = Solution.findKthLargest(nums, k)
	print (result)

main()