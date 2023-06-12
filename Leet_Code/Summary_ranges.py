class Solution:
	def summaryRanges(nums :list) -> list:
		index = 1
		in_range_list = []
		i = 0
		j = 0
		start = 0
		end = 0
		while (i < len(nums)):
			start = nums[i]
			while (i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]):
				i += 1
			end = nums[i]
			if start == end:
				in_range_list.append(str(start))
			else:
				in_range_list.append(str(start) + "->" + str(end))
			i += 1
		return (in_range_list)




		# for i in nums:
		# 	for j in nums:
		# 		print (i, j)
		# 		if (i + index == j): 
		# 			print (f"this ?{i, j}")
		# 			in_range_list.append(i)
		# 			in_range_list.append(j)

		# print (in_range_list)
		# for number in in_range_list:

					
	
def main ():
	nums = [0,1,2,4,5,7]
	# nums = [0,2,3,4,6,8,9]
	result = []
	result = Solution.summaryRanges(nums)

main()