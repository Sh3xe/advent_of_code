import re

sequences = []

with open("input") as file:
	lines = file.read().split("\n")
	for line in lines:
		if line == "":
			continue
		sequences.append( [int(num) for num in line.split(" ")] )

sum = 0

for seq in sequences:
	vals = [seq]
	done = False
	while not done:
		val = []
		s = vals[-1]
		done = True
		for i in range(len(vals[-1]) - 1):
			val.append(-s[i] + s[i+1])
			if -s[i] + s[i+1] != 0:
				done = False
		vals.append(val)
	
	#print(vals)
	vals[-1].insert(0, 0)
	for j in range(1, len(vals)):
		#print(len(vals) - j - 1, end=" ")
		#k - vals[len(vals) - i - 1][-1] = vals[len(vals) - i]
		vals[len(vals)-1-j].insert(0, vals[len(vals) - j - 1][0] - vals[len(vals) - j][0] )
	#print(vals)

	sum += vals[0][0]

print(sum)