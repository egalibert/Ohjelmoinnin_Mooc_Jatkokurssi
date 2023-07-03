class Solution:
	def buddyStrings(s: str, goal: str) -> bool:
		ns = len(s)
		ng = len(goal)

		if ns != ng:
			return False
		
		if s == goal:
			temp = set(s)
			print(s, temp)
			return len(temp) < len(goal)
		
		i = 0
		j = ns - 1

		while i < j and s[i] == goal[i]:
			i += 1

		while j >= 0 and s[j] == goal[j]:
			j -= 1

		if i < j:
			s_list = list(s)
			s_list[i], s_list[j] = s_list[j], s_list[i]
			s = ''.join(s_list)

		return s == goal
    
def main():
	s = "ab"
	goal = "ab"
	result = False
	result = Solution.buddyStrings(s, goal)

main()