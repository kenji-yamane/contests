def read_line():
	x = input().strip().split(' ')
	return [int(i) for i in x]

def beautify(arr):
	answers = [0]
	for i in range(0, len(arr), 2):
		if i < len(arr) - 1:
			answers[0] += arr[i + 1] - arr[i]
	if len(arr)%2 == 0:
		return answers[0]

	backwards = 0
	forwards = answers[0]
	for i in range(len(arr) - 1, 1, -2):
		backwards += arr[i] - arr[i - 1]
		forwards -= arr[i - 1] - arr[i - 2]
		answers.append(backwards + forwards)
	return min(answers)

t = int(input())

for _ in range(t):
	n, k = read_line()
	a = read_line()

	temp = [[el%k, el] for el in a]
	temp.sort(key = lambda x : (x[0], x[1]))
	modulo_split = {}
	for el in temp:
		modulo = el[0]
		if modulo not in modulo_split:
			modulo_split[modulo] = []
		modulo_split[modulo].append(el[1])

	odds = 0
	for modulo in modulo_split:
		if len(modulo_split[modulo])%2 == 1:
			odds += 1
		if odds > 1:
			break
		#modulo_split[modulo].sort()
	if odds > 1:
		print(-1)
		continue

	answer = 0
	for modulo in modulo_split:
		answer += beautify(modulo_split[modulo])//k
	print(answer)

