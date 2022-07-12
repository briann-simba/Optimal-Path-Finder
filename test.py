x = [(1, True), (2, False), (3, False)]

for i in range(len(x)):
	if x[i][0] != 2:
		x[i] = (x[i][0], False)
	else:
		x[i] = (x[i][0], True)

print(x)
