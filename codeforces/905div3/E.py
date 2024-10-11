def read_numbers():
	line = input().strip().split(' ')
	numbers = [int(i) for i in line]
	return numbers

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_numbers()

	num_bits = []
	for el in a:
		num_bits.append(0)
		while el > 0:
			num_bits[-1] += 1
			el >>= 1

	ans = 0
	num_dups = [0]*n
	for idx in range(1, n):
		previous_bits = num_bits[idx - 1] + num_dups[idx - 1]
		if previous_bits > num_bits[idx]:
			ans += previous_bits - num_bits[idx]
			num_dups[idx] = previous_bits - num_bits[idx]
		if previous_bits == num_bits[idx] + num_dups[idx]:
			previous_corrected = (a[idx - 1] << max(num_bits[idx] - num_bits[idx - 1], 0))
			current_corrected = (a[idx] << max(num_bits[idx - 1] - num_bits[idx], 0))
			if previous_corrected > current_corrected:
				ans += 1
				num_dups[idx] += 1
	print(ans)

