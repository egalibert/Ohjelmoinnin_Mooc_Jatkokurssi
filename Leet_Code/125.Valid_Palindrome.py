class Solution:
	def isPalindrome(s: str) -> bool:
		str1 = ""
		str2 = ""
		
		for letter in s:
			if (letter.isalnum()):
				str1 += letter.lower()

		i = len(s) - 1
		while (i >= 0):
			if(s[i].isalnum()):
				str2 += s[i].lower()
			i -= 1

		if (str1 == str2):
			return (True)
		return (False)
		
def main():
	s = "A man, a plan, a canal: Panama"
	# s = "race a car"
	result = False
	result = Solution.isPalindrome(s)
	print (result)

main()