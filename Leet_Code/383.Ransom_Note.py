# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
from collections import Counter

class Solution:
	def canConstruct(ransomNote: str, magazine: str) -> bool:
		rNote, maga = Counter(ransomNote), Counter(magazine)

		if (rNote & maga == rNote):
			return True
		return False
		

def main():
	ransomNote = "aa"
	magazine = "ab"

	result = False

	result = Solution.canConstruct(ransomNote, magazine)
	print(result)

main()