class Solution:
	def strStr(haystack: str, needle: str) -> int:
		for i in range(0, len(haystack)):
			for j in range(i, len(haystack)):
				print(haystack[i:j + 1])
				if (haystack[i:j + 1] == needle):
					return (i)

		return -1

	
def main():
	haystack = "sadbutsad"
	needle = "sad"
	
	result = 0
	result = Solution.strStr(haystack, needle)

main()
