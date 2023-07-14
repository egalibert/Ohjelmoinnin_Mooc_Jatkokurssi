class Solution:
	def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
		for i in range(n):
			nums1[m+i] = nums2[i]
		nums1.sort()

def main():
	nums1 = [1,2,3,0,0,0]
	m = 3
	nums2 = [2,5,6]
	n = 3

	result = Solution.merge(nums1, m, nums2, n)