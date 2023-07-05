class Solution:
	def longestSubarray(nums: list) -> int:
		left = 0  # left boundary of the window
		right = 0  # right boundary of the window
		zero_count = 0  # count of zeros encountered
		max_length = 0  # maximum length of subarray with only 1's

		while right < len(nums):
			if nums[right] == 0:
				zero_count += 1

			while zero_count > 1:
				if nums[left] == 0:
					zero_count -= 1
				left += 1

			max_length = max(max_length, right - left)

			right += 1

		return max_length


def main():
	# nums = [1, 0, 1, 1]
	nums = [0,1,1,1,0,1,1,0,1]
	result = 0
	result = Solution.longestSubarray(nums)

	print (result)

main ()


# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.