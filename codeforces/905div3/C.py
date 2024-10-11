def read_numbers():
	line = input().strip().split(' ')
	numbers = [int(i) for i in line]
	return numbers

t = int(input())

for _ in range(t):
	n, k = read_numbers()
	a = read_numbers()

	mod_freq = [0]*k
	for el in a:
		mod_freq[el%k] += 1

	if mod_freq[0] > 0:
		print(0)
		continue

	if k == 4:
		if mod_freq[2] > 1:
			print(0)
		elif mod_freq[3] > 0:
			print(1)
		elif mod_freq[2] > 0 and n > 1:
			print(1)
		elif mod_freq[2] > 0:
			print(2)
		elif n > 1:
			print(2)
		else:
			print(3)
		continue

	max_mod = 0
	for idx, freq in enumerate(mod_freq):
		if freq > 0:
			max_mod = idx
	print(k - max_mod)

