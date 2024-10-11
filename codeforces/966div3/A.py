def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	a = input().strip()

	if len(a) <= 2 or a[0] != '1' or a[1] != '0' or a[2] == '0':
		print('no')
		continue
	if len(a) == 3 and a[2] == '1':
		print('no')
		continue
	print('yes')

