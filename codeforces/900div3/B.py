t = int(input())

for _ in range(t):
	n = int(input())
	arr = [2, 3]
	for _ in range(n - 2):
		if (3*arr[-1] + 3)%(arr[-1] + arr[-2]) == 0:
			arr.append(arr[-1] + 2)
		else:
			arr.append(arr[-1] + 1)
	print(*arr)
