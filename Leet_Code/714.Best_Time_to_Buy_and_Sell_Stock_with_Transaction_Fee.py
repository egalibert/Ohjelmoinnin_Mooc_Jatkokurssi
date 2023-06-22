class Solution:
	def maxProfit(prices :list, fee: int) -> int:
		new_list = []
		new_list = sorted(prices)
		first = 0
		total_p = 0
		last = len(prices) - 1
		print(new_list, first, last)
		while (True):
			print(f"Current stocks are {new_list[first]} and {new_list[last]} and total profit is {total_p}")
			if (new_list[first] + 2 < new_list[last]):
				total_p += new_list[last] - (new_list[first] + 2)
				first += 1
				last -= 1
			else:
				break
		print(total_p)

def main():
	prices = [1,3,2,8,4,9]
	fee = 2
	result = 0
	result = Solution.maxProfit(prices, fee)
	print(result)

main()