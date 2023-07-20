# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

class Solution:
	def lengthOfLastWord(s: str) -> int:
		new_list = []
		new_list = s.split()
		return (len(new_list[len(new_list) - 1]))
	
def main():
	s = "Hello World"
	# s = "   fly me   to   the moon  "
	result = 0
	result = Solution.lengthOfLastWord(s)
	
main()