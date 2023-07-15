class Solution:
	def removeElement(nums: list, val: int) -> int:
		i = 0
		while (i < len(nums)):
			if (nums[i] == val):
				nums.pop(i)
				i -= 1
			i += 1

		return len(nums)

def main():
	nums = [0,1,2,2,3,0,4,2]
	val = 2
	result = 0
	result =  Solution.removeElement(nums, val)

main()