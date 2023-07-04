class Solution:
    def singleNumber(nums: list) -> int:
        result = 0
        for num in nums:
            if (nums.count(num) < 3):
                result = num
        return (result)


def main():
    # nums = [2,2,3,2]
    nums = [0,1,0,1,0,1,99]
    result = 0
    result = Solution.singleNumber(nums)

    print (result)

main()