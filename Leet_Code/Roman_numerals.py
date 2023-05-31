
class Solution:
	def romanToInt(s: str) -> int:
		result = 0
		values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

		s = s.replace("IV", "IIII").replace("IX", "VIIII")
		s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
		s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

		for letter in s:
			result += values[letter]
		return(result)


def main():
	s = "MCMXCIV"
	
	output = Solution.romanToInt(s)
	print(f"{s} = {output}")

main()