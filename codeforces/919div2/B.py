def read_array():
	arr = input().strip().split(' ')
	arr = [int(i) for i in arr]
	return arr

t = int(input())

for _ in range(t):
	n, k, x = read_array()
	a = read_array()
	a.sort(reverse=True)
	gain = 0
	max_gain = 0
	for i in range(k):
		gain += a[i]
		if i + x < len(a):
			gain -= 2*a[i + x]
		max_gain = max(max_gain, gain)
	print(sum(a[x:len(a)]) - sum(a[0:x]) + max_gain)
