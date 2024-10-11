def read_line():
	x = input().strip()
	return [int(i) for i in x]

def compute(arr):
	answer = arr[0]
	for idx in range(len(arr) - 1):
		answer = min(answer + arr[idx + 1], answer*arr[idx + 1])
	return answer

t = int(input())

for _ in range(t):
	n = int(input())
	s = read_line()

	answers = []
	for i in range(len(s) - 1):
		arr = s[0:i] + [10*s[i] + s[i + 1]] + s[i + 2:len(s)]
		answers.append(compute(arr))
	print(min(answers))

