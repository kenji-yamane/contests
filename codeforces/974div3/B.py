# n even: true false false true false false true
# n odd: false false true true false false true

def read_line():
	line = input().strip().split(' ')
	return [int(el) for el in line]

t = int(input())

for _ in range(t):
	n, k = read_line()
	answer = [[True, False, False, True], [False, False, True, True]]
	if answer[n%2][(k - 1)%4]:
		print('yes')
	else:
		print('no')

