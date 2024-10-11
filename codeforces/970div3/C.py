def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def best_arr(interval):
	ini, fin = 0, interval
	if fin*(fin + 1)//2 <= interval:
		return fin + 1

	while ini + 1 != fin:
		middle = (ini + fin)//2
		if middle*(middle + 1)//2 > interval:
			fin = middle
		else:
			ini = middle
	return ini + 1

t = int(input())

for _ in range(t):
	l, r = read_line()
	print(best_arr(r - l))

