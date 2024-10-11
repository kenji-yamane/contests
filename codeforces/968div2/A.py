def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	s = input().strip()
	if s[0] == s[-1]:
		print('no')
	else:
		print('yes')

