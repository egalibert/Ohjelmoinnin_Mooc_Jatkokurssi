class Solution(object):
	def fizzBuzz(self, n):
		i = 1
		nl = []
		while (i <= n):
			if (i % 3 == 0 and i % 5 == 0):
				nl.append("FizzBuzz")
			elif (i % 3 == 0 and i % 5 != 0):
				nl.append("Fizz")
			elif (i % 3 != 0 and i % 5 == 0):
				nl.append("Buzz")
			else:
				nl.append(str(i))
			i += 1
		return (nl)

	def main():
		n = 15
		lista = []
		lista = fizzbuzz(n)
		print(lista)