
class Solution:
	def removeDuplicates(nums: list) -> int:
		j = 1
		for i in range(1, len(nums)):
			print(f"current values are i = {nums[i]} and i2 = {nums[j]}")
			if nums[i] != nums[i - 1]:
				nums[j] = nums[i]
				j += 1
		return j

	
def main():
	nums = [0,0,1,1,1,2,2,3,3,4]
	result = 0
	result = Solution.removeDuplicates(nums)

	print (result)

main()


		# while (i < len(nums)):
		# 	i2 = i + 1
		# 	while (i2 < len(nums)):
		# 		print(f"current values are i = {nums[i]} and i2 = {nums[i2]}")
		# 		if (nums[i] == nums[i2]):
		# 			nums.pop(i2)
		# 		i2 += 1
		# 		print (i, i2)
		# 	i += 1
		
		# print (nums)