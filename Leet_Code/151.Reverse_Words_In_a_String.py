class Solution:
	def reverseWords(s: str) -> str:
		str = ""
		str = s.split()
		result = ""
		print (str)
		i = len(str) - 1
		while (i >= 0):
			result += str[i]
			if (i != 0):
				result += " "
			i -= 1
		return result
	
def main():
	s = "  hello world  "
	result  = ""
	result = Solution.reverseWords(s)

main()