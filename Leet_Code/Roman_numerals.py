

def romanToInt(s :str):
	total = 0
	i = 0

	while (i < len(s)):
		if s[i] == 'I':
			total += 1
		i += 1
	print(total)
	return (total)

def main():
	s = "III"
	
	output = romanToInt(s)
	print(f"{s} = {output}")

main()