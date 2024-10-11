def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n = int(input())
	b = list(input().strip())
	r = list(set(b))
	r.sort()
	decoder = {}
	for idx in range(len(r)):
		decoder[r[idx]] = r[len(r) - idx - 1]
	s = [decoder[el] for el in b]
	print(''.join(s))

