import re 

lines = []

with open("input") as file:
	lines = file.read().split("\n")

li = len(lines)
lj = len(lines[0])

empty_rows = []
for i in range(li):
	empty = True
	for j in range(lj):
		if lines[i][j] != ".":
			empty = False
	if empty:
		empty_rows.append(i)

empty_cols = []
for j in range(lj):
	empty = True
	for i in range(li):
		if lines[i][j] != ".":
			empty = False
	if empty:
		empty_cols.append(j)

positions = []
for j in range(li):
	for i in range(lj):
		if lines[i][j] == "#":
			positions.append((i,j))

EXPAND = 1000000 - 1

dists = []
print(empty_cols, empty_rows)
for p0 in range(len(positions)):
	for p1 in range(len(positions)):
		a, b = positions[p1]
		c, d = positions[p0]
		if p1 != p0:
			num_empty_cols = 0
			for j in range(min(b, d), max(b,d)):
				if j in empty_cols:
					num_empty_cols += 1
			num_empty_rows = 0
			for i in range(min(a, c), max(a,c)):
				if i in empty_rows:
					num_empty_rows += 1
			dists.append(abs(a-c) + abs(b-d) + EXPAND*num_empty_cols + EXPAND*num_empty_rows)

print(sum(dists) // 2)