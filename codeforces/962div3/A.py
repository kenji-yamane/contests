def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())

	ans = n//4 + (n%4)//2
	print(ans)

