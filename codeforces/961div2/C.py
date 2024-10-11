# x**(2**n)
# y**(2**m)

# 2**n(logx) >= 2**m(logy)
# nlog2 + loglogx >= mlog2 + loglogy
# n >= (mlog2 + loglogy - loglogx)/log2
# n >= m + log_2(log_x(y))
# log_x(y) = 2**p
# y = x**(2**p)
# x = y**forward_pow

from math import log, ceil

def read_line():
	line = input().strip().split(' ')
	return [int(i) for i in line]

t = int(input())

for _ in range(t):
	n = int(input())
	a = read_line()

	justice = [0]
	for i in range(1, len(a)):
		if a[i] == a[i - 1]:
			justice.append(justice[-1])
			continue
		if a[i] == 1:
			justice.append(-1)
			break
		if a[i - 1] == 1:
			justice.append(0)
			continue

		justice.append(ceil(justice[-1] + log(log(a[i - 1])/log(a[i]))/log(2)))
		justice[-1] = max(justice[-1], 0)

	if justice[-1] == -1:
		print(-1)
	else:
		print(sum(justice))

