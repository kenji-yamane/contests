def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

def only_ones(s):
	if len(s) == 4:
		print('Yes')
	else:
		print('No')

t = int(input())

for _ in range(t):
	n = int(input())
	s = input().strip()

	first_zero = len(s)
	for i in range(len(s)):
		if s[i] == '0':
			first_zero = i
			break
	if first_zero == len(s):
		only_ones(s)
		continue

	row_len = first_zero - 1
	if len(s)//row_len == row_len:
		print('Yes')
	else:
		print('No')

