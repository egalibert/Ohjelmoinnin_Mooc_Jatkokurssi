import collections

class Solution:
	def maxConsecutiveAnswers(answerKey, k):
		max_freq = 0
		i = 0
		char_count = collections.Counter()

		for j in range(len(answerKey)):

			char_count[answerKey[j]] += 1
			max_freq = max(max_freq, char_count[answerKey[j]])
			if j - i + 1 > max_freq + k:
				char_count[answerKey[i]] -= 1
				i += 1


		return len(answerKey) - i
		

	
def main():
	answerKey = "TTFF"
	k = 2
	result = 0
	result = Solution.maxConsecutiveAnswers(answerKey, k)

main()