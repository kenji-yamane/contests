from math import gcd

def read_numbers():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

def operation(x, y):
	return gcd(x, y) + y

t = int(input())

for _ in range(t):
	x = int(input())
	ans = 0
	ans_y = 0
	for i in range(1, x):
		if operation(x, i) > ans:
			ans = operation(x, i)
			ans_y = i
	print(ans_y)

