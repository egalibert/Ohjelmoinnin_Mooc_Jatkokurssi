class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		s = s.split(' ')
		return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s))) and len(pattern) == len(s)
	
def main():
	pattern = "abba"
	s = "dog cat cat dog"
	
	result = False
	result = Solution.wordPattern(pattern, s)