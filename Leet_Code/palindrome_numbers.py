class Solution:
	def isPalindrome(x: int) -> bool:
		newlist = []
		index = 0
		string = str(x)
		print(string)
		for i in range(len(string)):
			newlist.append(string[i])
		print(newlist)
		takaa = len(newlist) - 1
		while (index < len(newlist)):
			if (newlist[index] != newlist[takaa]):
				return (False)
			else:
				index += 1
				takaa -= 1
		return (True)

def main():
	x = -121
	tulos = Solution.isPalindrome(x)
	print(tulos)

main()