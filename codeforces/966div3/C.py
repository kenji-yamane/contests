def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	m = int(input())
	for _ in range(m):
		s = input().strip()
		if len(s) != len(a):
			print('no')
			continue

		mapping = [None]*26
		match = True
		for idx, el in enumerate(s):
			if mapping[ord(el) - ord('a')] == None:
				mapping[ord(el) - ord('a')] = a[idx]
			if mapping[ord(el) - ord('a')] != a[idx]:
				match = False
		present = {}
		for el in mapping:
			if el == None:
				continue
			if el not in present:
				present[el] = True
			else:
				match = False
		if match:
			print('yes')
		else:
			print('no')

