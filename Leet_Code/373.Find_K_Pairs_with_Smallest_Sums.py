import heapq

class Solution:
	def kSmallestPairs(nums1, nums2, k):
		result_list = []
		if not nums1 or not nums2 or not k:
			return result_list
		
		heap = []
		visited = set()
		
		heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
		
		visited.add((0, 0))
		
		while k and heap:
			print (heap)
			_, i, j = heapq.heappop(heap)
			result_list.append([nums1[i], nums2[j]])
			print (heap)
			
			if i + 1 < len(nums1) and (i + 1, j) not in visited:
				heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
				visited.add((i + 1, j))
			
			if j + 1 < len(nums2) and (i, j + 1) not in visited:
				heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
				visited.add((i, j + 1))
			k -= 1
		
		return result_list



def main():
	# nums1 = [1,7,11]
	# nums2 = [2,4,6]
	# k = 3

	# nums1 = [1,1,2]
	# nums2 = [1,2,3]
	# k = 2
	
	nums1 = [1,2]
	nums2 = [3]
	k = 3


	result_listult = 0
	result_listult = Solution.kSmallestPairs(nums1, nums2, k)

	print(result_listult)

main()





	# def kSmallestPairs(nums1: list, nums2: list, k: int) -> list:
	# 	x = 0
	# 	j = 0
	# 	result_listult_list = []
	# 	if len(nums1) < k or len(nums2) < k:
	# 		if len(nums1) > len(nums2):
	# 			k = len(nums1)
	# 		else:
	# 			k = len(nums2)
	# 	while (k > 0):
	# 		print(nums1[x], nums2[j])
	# 		pair = []
	# 		if (nums1[x] < nums2[j]):
	# 			pair = [nums1[x], nums2[j]]
	# 			result_listult_list.append(pair)
	# 			if (nums1[x + 1] < nums2[j + 1] and x < len(nums1)):
	# 				x += 1
	# 			elif nums2[j + 1] < nums1[x + 1] and j < len(nums2):
	# 				j += 1
	# 			k -= 1
	# 		elif (nums2[j] < nums1[x]):
	# 			pair = [nums2[j], nums1[x]]
	# 			result_listult_list.append(pair)
	# 			if (nums1[x + 1] < nums2[j + 1] and x < len(nums1)):
	# 				x += 1
	# 			elif nums2[j + 1] < nums2[j + 1] and j < len(nums2):
	# 				j += 1
	# 			k -= 1
	# 		elif (nums1[x] == nums2[j]):
	# 			pair = [nums2[j], nums1[x]]
	# 			result_listult_list.append(pair)
	# 			if (nums1[x + 1] < nums2[j + 1] and x < len(nums1)):
	# 				x += 1
	# 			elif nums2[j + 1] < nums1[x + 1] and j < len(nums2):
	# 				j += 1
	# 			k -= 1
	# 	print (result_listult_list)
