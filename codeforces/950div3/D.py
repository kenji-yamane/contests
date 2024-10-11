from math import gcd

def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

def gcd_sequence(arr):
	ans = []
	for i in range(1, len(arr)):
		ans.append(gcd(arr[i], arr[i - 1]))
	return ans

def non_decreasing(arr):
	for i in range(1, len(arr)):
		if arr[i] < arr[i - 1]:
			return False
	return True

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	gcd_a = gcd_sequence(a)
	if non_decreasing(gcd_a):
		print('yes')
		continue

	to_remove = None
	for i in range(1, n - 1):
		if gcd_a[i] < gcd_a[i - 1]:
			to_remove = [i - 1, i, i + 1]
			break

	possible = False
	for idx in to_remove:
		arr = a.copy()
		arr.pop(idx)
		if non_decreasing(gcd_sequence(arr)):
			possible = True

	if possible:
		print('yes')
	else:
		print('no')
