def read_numbers():
	line = input().strip().split(' ')
	numbers = [int(i) for i in line]
	return numbers

t = int(input())

for _ in range(t):
	n, k = read_numbers()
	s = input().strip()

	letter_freq = {}
	for letter in s:
		if letter not in letter_freq:
			letter_freq[letter] = 0
		letter_freq[letter] += 1

	odds = 0
	for key, value in letter_freq.items():
		if value%2 == 1:
			odds += 1
	if odds - k > 1:
		print('NO')
	else:
		print('YES')
