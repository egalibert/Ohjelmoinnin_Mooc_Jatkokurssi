class Solution:
	def twosum(nums :list, target :int):
		newlist = []
		result = []
		i = 0

		# for i in range(len(nums)):
		# 	if nums[i] <= target:
		# 		newlist.append(nums[i])

		for i in range(len(newlist)):
			for x in range(len(newlist)):

				if (nums[i] + nums[x] == target and x != i):
					result.append(i)
					result.append(x)

					return (result)

		
def main():
	nums = [0, 4, 3, 0]
	i = 0
	target = 0
	result = []
	result = Solution.twosum(nums, target)

main()