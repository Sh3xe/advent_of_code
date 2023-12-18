import re

tiles = []
distances = []
s_pos = (0, 0)

with open("input") as file:
	lines = file.read().split("\n")
	tiles = lines
	for i in range(len(tiles)):
		if tiles[i] == "":
			continue
		for j in range(len(tiles[0])):
			if tiles[i][j] == "S":
				s_pos = (i, j)


li = len(tiles)
lj = len(tiles[0])

def neighs(i, j):
	global li, lj, tiles
	c = tiles[i][j]
	res = []
	if c == "|":
		if tiles[i+1][j] in "S|LJ":
			res.append((i+1, j))
		if tiles[i-1][j] in "S|F7":
			res.append((i-1, j))
	elif c == "-":
		if tiles[i][j+1] in "S-7J":
			res.append((i, j+1))
		if tiles[i][j-1] in "S-FL":
			res.append((i, j-1))
	elif c == "L":
		if tiles[i-1][j] in "S|7F":
			res.append((i-1, j))
		if tiles[i][j+1] in "S-J7":
			res.append((i, j+1))
	elif c == "J":
		if tiles[i-1][j] in "S|F7":
			res.append((i-1, j))
		if tiles[i][j-1] in "S-FL":
			res.append((i, j-1))
	elif c == "7":
		if tiles[i+1][j] in "S|JL":
			res.append((i+1, j))
		if tiles[i][j-1] in "S-FL":
			res.append((i, j-1))
	elif c == "F":
		if tiles[i+1][j] in "S|JL":
			res.append((i+1, j))
		if tiles[i][j+1] in "S-J7":
			res.append((i, j+1))
		res = [(i+1, j), (i, j+1)]
	elif c == ".":
		res = []
	elif c == "S":
		if tiles[i+1][j] in "S|JL":
			res.append((i+1, j))
		if tiles[i][j+1] in "S-J7":
			res.append((i, j+1))
		if tiles[i-1][j] in "S|7F":
			res.append((i-1, j))
		if tiles[i][j-1] in "S-FL":
			res.append((i, j-1))
	rr = []
	for (ri, rj) in res:
		if (0 <= ri < li and 0 <= rj < lj):
			rr.append((ri, rj))
	return rr

def ptos(pos):
	a, b = pos
	return f"{a}-{b}"

def skey(u):
	_, _, k = u
	return -k

for i in range(li):
	distances.append( [-1] * lj )

a, b = s_pos
positions = [(a, b, 0)]
in_brace = []
while len(positions) != 0:
	positions = sorted(positions, key=skey)
	(ci, cj, d) = positions.pop()
	
	if distances[ci][cj] != -1:
		continue

	in_brace.append((ci, cj))

	distances[ci][cj] = d

	for (i, j) in neighs(ci, cj):
		positions.append((i, j, d+1))

new_tiles = []
for i in range(li):
	new_tiles.append(["."]*3*lj)
	new_tiles.append(["."]*3*lj)
	new_tiles.append(["."]*3*lj)

for i in range(li):
	for j in range(lj):
		if (i, j) not in in_brace:
			continue
		if tiles[i][j] == "|":
			new_tiles[3*i+1][3*j+1] = "|"
			new_tiles[3*i-1+1][3*j+1] = "|"
			new_tiles[3*i+1+1][3*j+1] = "|"
		if tiles[i][j] == "-":
			new_tiles[3*i+1][3*j+1] = "-"
			new_tiles[3*i+1][3*j-1+1] = "-"
			new_tiles[3*i+1][3*j+1+1] = "-"
		if tiles[i][j] == "L":
			new_tiles[3*i+1][3*j+1] = "L"
			new_tiles[3*i-1+1][3*j+1] = "|"
			new_tiles[3*i+1][3*j+1+1] = "-"
		if tiles[i][j] == "J":
			new_tiles[3*i+1][3*j+1] = "J"
			new_tiles[3*i-1+1][3*j+1] = "|"
			new_tiles[3*i+1][3*j-1+1] = "-"
		if tiles[i][j] == "7":
			new_tiles[3*i+1][3*j+1] = "7"
			new_tiles[3*i+1+1][3*j+1] = "|"
			new_tiles[3*i+1][3*j-1+1] = "-"
		if tiles[i][j] == "F":
			new_tiles[3*i+1][3*j+1] = "F"
			new_tiles[3*i+1+1][3*j+1] = "|"
			new_tiles[3*i+1][3*j+1+1] = "-"
		if tiles[i][j] == "S":
			new_tiles[3*i+1][3*j+1] = "S"
			new_tiles[3*i+1+1][3*j+1] = "S"
			new_tiles[3*i+1][3*j+1+1] = "S"
			new_tiles[3*i-1+1][3*j+1] = "S"
			new_tiles[3*i+1][3*j-1+1] = "S"

def search_from(i, j):
	global new_tiles
	l = [(i,j)]
	while len(l) != 0:
		a, b = l.pop()
		if new_tiles[a][b] != ".":
			continue

		new_tiles[a][b] = "#"
		for i0 in range(-1, 2):
			for j0 in range(-1, 2):
				if 0 <= a+i0 < 3*li and 0 <= b+j0 < 3*lj:
					l.append((a+i0, b+j0))

for i in range(3*li):
	search_from(i, 0)
	search_from(i, 3*lj-1)

for j in range(3*lj):
	search_from(0, j)
	search_from(3*li-1, j)


s = 0
for i in range(li):
	for j in range(lj):
		if new_tiles[3*i+1][3*j+1] == ".":
			s += 1

print(s)

for t in new_tiles:
	for a in t:
		print(a, end="")
	print()