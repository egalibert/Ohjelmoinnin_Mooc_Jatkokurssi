# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

class Solution:
	def combine(n: int, k: int) -> list[list]:
		i = 1
		j = 1
		new_list = []
		if (n and k == 1):
			return [1]
		while (i <= k):
			j = 1
			while (j <= n):
				if (i != j and [i, j] not in new_list):
					new_list.append([i, j])
				j += 1
			i += 1

		# print (new_list)
		return (new_list)


def main():
	n = 4
	k = 2
	result = []
	result = Solution.combine(n, k)

	print (result)

main()