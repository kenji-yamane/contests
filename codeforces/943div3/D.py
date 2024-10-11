def read_line():
	line = input().strip().split(' ')
	line = [int(i) for i in line]
	return line

def optimal_strategy(a, p, k, ini):
	strategies = [a[ini]*k]
	points_so_far = a[ini]
	curr = p[ini]
	k -= 1

	while k > 0 and curr != ini:
		strategies.append(points_so_far + a[curr]*k)
		points_so_far += a[curr]
		curr = p[curr]
		k -= 1
	return max(strategies)

t = int(input())

for _ in range(t):
	n, k, pb, ps = read_line()
	temp = read_line()
	p = [el - 1 for el in temp]
	pb -= 1
	ps -= 1

	a = read_line()
	bodya = optimal_strategy(a, p, k, pb)
	sasha = optimal_strategy(a, p, k, ps)
	if bodya > sasha:
		print('Bodya')
	elif sasha > bodya:
		print('Sasha')
	else:
		print('Draw')

