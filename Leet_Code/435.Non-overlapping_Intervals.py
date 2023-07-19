# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of 
# intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution:
	def eraseOverlapIntervals(self, intervals: list[list]) -> int:
		intervals.sort(key=lambda x: x[1])
		n = len(intervals)

		prev = 0
		count = 1

		for i in range(1, n):
			if intervals[i][0] >= intervals[prev][1]:
				prev = i
				count += 1

		return n - count

def main():
	intervals = [[1,2],[2,3],[3,4],[1,3]]
	result = 0
	result = Solution.eraseOverlapIntervals(intervals)

main()