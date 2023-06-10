class Solution:
	def nextGreatestLetter(letters: list, target: str) -> str:
		if target == 'z':
			return (letters[0])
		for letter in letters:
			if letter > target:
				print(letter)
				return(letter)

def main():
	letters = ["c","f","j"]
	target = "c"

	result = Solution.nextGreatestLetter(letters, target)

main()
