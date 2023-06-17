class Solution:
	def makeArrayIncreasing(arr1 :list, arr2 :list) -> int:
		print(arr1)

		for i in range (len(arr1)):
			for j in range(i + 1, len(arr1)):
				print(arr1[i], arr1[j])
				if (arr1[i] > arr1[j]):
					for x in arr2:
						print (x)
						if x < arr1[j] and x > arr1[i - 1]:
							arr1[i] = x
							print (arr1)

def main():
	arr1 = [1,5,3,6,7]
	# arr2 = [1,3,2,4]
	arr2 = [4,3,1]

	result = 0
	result = Solution.makeArrayIncreasing(arr1, arr2)

	print (result)

main()