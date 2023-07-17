# Given an integer numsay nums, rotate the arrsay to the right by k steps, where k is non-negative.


# class Solution:
# 	def rotate(nums: list, k: int) -> None:
# 		n = len(nums)
# 		temp = []
# 		i = 0
# 		while (i < k):
# 			temp.append(nums[i])
# 			i = i + 1
# 		i = 0
# 		while (k < n):
# 			nums[i] = nums[k]
# 			i = i + 1
# 			k = k + 1
# 		nums[:] = nums[: i] + temp
# 		return nums

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a)

    
def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    result = 0
    result = Solution.rotate(nums, k)
    print (result)
    

main()