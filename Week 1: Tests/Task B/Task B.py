a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == 0) and (b != 0) and (c != 0) and (d != 0) and (c < d):
	print(1, min(c, d) + 1)
elif (a == 0) and (b != 0) and (c != 0) and (d != 0) and (c >= d):
	print(1, max(c, d) + 1)
elif (a != 0) and (b == 0) and (c != 0) and (d != 0) and (c > d):
	print(1, min(c, d) + 1)
elif (a != 0) and (b == 0) and (c != 0) and (d != 0) and (c <= d):
	print(1, max(c, d) + 1)

elif (a != 0) and (b != 0) and (c == 0) and (d != 0) and (a > b):
	print(max(a, b) + 1, 1)
elif (a != 0) and (b != 0) and (c == 0) and (d != 0) and (a <= b):
	print(min(a, b) + 1, 1)
elif (a != 0) and (b != 0) and (c != 0) and (d == 0) and (a < b):
	print(max(a, b) + 1, 1)
elif (a != 0) and (b != 0) and (c != 0) and (d == 0) and (a >= b):
	print(min(a, b) + 1, 1)

elif (a == 0 and c == 0) or (b == 0 and d == 0):
	print(1, 1)

else:
	if (min(a, b) + min(c, d) < max(a, b)) and (min(a, b) + min(c, d) < max(c, d)) and (a > b) and (c > d):
		print(min(a, b) + 1, min(c, d) + 1)
	elif (min(a, b) + min(c, d) < max(a, b)) and (min(a, b) + min(c, d) < max(c, d)) and (a <= b) and (c <= d):
		print(min(a, b) + 1, min(c, d) + 1)

	elif (min(a, b) + min(c, d) < max(a, b)) and (min(a, b) + min(c, d) < max(c, d)) and (a > b) and (c <= d):
		print(1, max(c, d) + 1)
	elif (min(a, b) + min(c, d) < max(a, b)) and (min(a, b) + min(c, d) < max(c, d)) and (a <= b) and (c > d):
		print(max(a, b) + 1, 1)

	elif (max(a, b) < min(a, b) + min(c, d)) and (max(a, b) < max(c, d)):
		print(max(a, b) + 1, 1)
	else:
		print(1, max(c, d) + 1)
