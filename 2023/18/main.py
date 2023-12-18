import re

def parse_input(path="test_input"):
	with open(path) as file:
		input = []
		for line in file.read().split("\n"):
			dir, num, col = re.findall("([A-Z]) (\\d+) \\((.*)\\)", line)[0]
			input.append((dir, int(num), col[1:]))
		return input

def get_delta(dir):
	return {
		"R": (0, 1),
		"L": (0, -1),
		"U": (-1, 0),
		"D": (1, 0),
	}[dir]

def part1(input):
	positions = [(0,0)]
	for (dir, num, col) in input:
		p = positions[-1]
		delta = get_delta(dir)
		for i in range(1, num+1):
			np = (p[0] + i*delta[0], p[1] + i*delta[1])
			positions.append(np)

	maxi, maxj = 0, 0
	mini, minj = 0, 0
	for (i, j) in positions:
		maxi = max(i, maxi)
		maxj = max(j, maxj)

		mini = min(i, mini)
		minj = min(j, minj)

	mi, mj = maxi - mini+1, maxj - minj+1

	trench_map = [["." for _ in range(mj)] for _ in range(mi)]
	for i, j in positions:
		trench_map[i-mini][j-minj] = "#"

	def neighs(i, j):
		dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		nei = []
		for (a, b) in dirs:
			if (0 <= i+a < mi) and (0 <= j+b < mj):
				nei.append((i+a,j+b))
		return nei

	def fill_from(i, j):
		lst = [(i,j)]
		while len(lst) != 0:
			a, b = lst.pop()
			if trench_map[a][b] != ".":
				continue
			trench_map[a][b] = " "
			for nei in neighs(a, b):
				lst.append(nei)

	# bucket fill...
	for i in range(mi):		
		fill_from(i, 0)
		fill_from(i, mj-1)

	for j in range(mj):		
		fill_from(0, j)
		fill_from(mi-1, j)

	# count
	

	for l in trench_map:
		for c in l:
			print(c, end="")
		print()

	total = 0
	for i in range(mi):
		for j in range(mj):
			if trench_map[i][j] != " ":
				total += 1
	print(total)

def part2(input):
	def convert(color):
		dir = ["R", "D", "L", "U"][int(color[-1])]
		dst = int("0x" + color[0:5], base=16)
		return dir, dst

	vertices = [(0, 0)]
	for _, _, col in input:
		dir, dst = convert(col)
		delta = get_delta(dir)
		pos = vertices[-1]
		vertices.append( (pos[0] + dst * delta[0], pos[1] + dst * delta[1]) )

	assert( vertices[0] == vertices[-1] )
	vertices.pop()

	boxes = []

	total = 0
	for (p0, p1) in boxes:
		di = abs(p1[0] - p0[0]) + 1
		dj = abs(p1[1] - p0[1]) + 1
		total += di*dj

	print(f"Total: {total}")

input = parse_input("test_input")
part2(input)