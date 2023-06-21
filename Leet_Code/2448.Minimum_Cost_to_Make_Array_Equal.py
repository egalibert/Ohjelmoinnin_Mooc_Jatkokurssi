class Solution:
	def minCost(nums :list, cost :list) -> int:
		total = 0
		for i in nums:
			total += i
		target = total // len(nums)
		total_cost = 0

		i = 0
		print(target)
		while (i < len(nums)):
			change = 0
			if (nums[i] != target):
				# print(f"At the start = {nums[i]} {target}")
				if nums[i] < target:
					while (nums[i] != target):
						nums[i] += 1
						change += 1
				if (nums[i] > target):
					while (nums[i] != target):
						nums[i] -= 1
						change += 1
			# print(f"After calculation = {nums[i]} {target}")
			total_cost += cost[i] * change
			i += 1
		return (total_cost)
		
def main ():
	# nums = [1,3,5,2]
	# cost = [2,3,1,14]

	nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
	cost = [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]

	result = 0
	result = Solution.minCost(nums, cost)

main()