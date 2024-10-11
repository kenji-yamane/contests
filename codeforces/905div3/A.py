t = int(input())

for _ in range(t):
	pin = input().strip()
	pin = [int(i) for i in pin]

	ans = 4
	curr = 1
	for digit in pin:
		if digit == 0:
			digit = 10
		ans += abs(digit - curr)
		curr = digit
	print(ans)
