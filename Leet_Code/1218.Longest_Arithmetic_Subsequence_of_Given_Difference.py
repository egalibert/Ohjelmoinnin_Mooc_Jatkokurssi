class Solution:
	def longestSubsequence(self, arr: list, difference: int) -> int:
		m = {}
		mx = 0
		for i in range(len(arr)):
			c = arr[i]
			if c - difference in m:
				m[c] = m[c - difference] + 1
			else:
				m[c] = 1
			mx = max(mx, m[c])
		return mx


	
def main():
	# arr = [1,2,3,4]
	arr = [1,5,7,8,5,3,4,2,1]
	difference = -2
	# difference = 1
	result = 0
	result = Solution.longestSubsequence(arr, difference)
	print (result)

main()