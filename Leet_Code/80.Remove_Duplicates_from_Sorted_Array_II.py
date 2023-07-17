class Solution:
	def removeDuplicates(nums: list) -> int:
		i = 0
		while (i < len(nums)):
			if (nums.count(nums[i]) > 2):
				nums.pop(i)
				i -= 1
			i += 1

		return len(nums)

def main():
	# nums = [1,1,1,2,2,3]
	nums = [0,0,1,1,1,1,2,3,3]
	result = 0
	result =  Solution.removeElement(nums)
	print(result)


main()