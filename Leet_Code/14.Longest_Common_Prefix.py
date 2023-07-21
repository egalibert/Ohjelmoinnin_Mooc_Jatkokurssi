# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
	def longestCommonPrefix(strs: list) -> str:
		ans = ''
		strs = sorted(strs)

		f_str = strs[0]
		l_str = strs[-1]
		for i in range(min(len(f_str),len(l_str))):
			if (f_str[i] != l_str[i]):
				return ans
			ans += f_str[i]
		return ans 

	
def main():
	strs = ["flower","flow","flight"]
	result = ""
	result = Solution.longestCommonPrefix(strs)

main()