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

TEST = [("R", 6, ""),
	("D", 5, ""),
	("L", 2, ""),
	("D", 2, ""),
	("R", 2, ""),
	("D", 2, ""),
	("L", 5, ""),
	("U", 2, ""),
	("L", 1, ""),
	("U", 2, ""),
	("R", 2, ""),
	("U", 3, ""),
	("L", 2, ""),
	("U", 2, "")]

# TEST = [("R", 100, ""),
# 	("U", 1, ""),
# 	("R", 10, ""),
# 	("D", 31, ""),
# 	("L", 110, ""),
# 	("U", 30, "")]

def part2(input):

	def convert(color):
		dir = ["R", "D", "L", "U"][int(color[-1])]
		dst = int("0x" + color[0:5], base=16)-
		return dir, dst

	vertices = [(0, 0)]
	for _,_, col in input:
		dir, dst = convert(col)
		delta = get_delta(dir)
		pos = vertices[-1]
		vertices.append( (pos[0] + dst * delta[0], pos[1] + dst * delta[1]) )

	def is_inside(i, j):
		count = 0
		for k in range(1, len(vertices)):
			p0, p1 = vertices[k-1], vertices[k]
			if p0[1] != p1[1]:
				continue
			ibeg = min(p0[0], p1[0]); iend = max(p0[0], p1[0])
			if ibeg <= i <= iend and p0[1] >= j:
				count += 1
		return count % 2 == 1

	print(vertices)

	# expand up every vertice whose normal is up
	for k in range(1, len(vertices)):
		p0, p1 = vertices[k-1], vertices[k]
		# horizontal vertices only
		if p1[0] != p0[0]:
			continue
		middle = ((p1[0]+p0[0]) /2), (p1[1]+p0[1]) /2
		if is_inside(middle[0]+0.5, middle[1]):
			vertices[k-1] = (vertices[k-1][0]-1, vertices[k-1][1])
			vertices[k] = (vertices[k][0]-1, vertices[k][1])

	vertices.pop()
	vertices.append(vertices[0])
	print(vertices)

	# expand left every vertice whose normal is right
	for k in range(1, len(vertices)):
		p0, p1 = vertices[k-1], vertices[k]
		# vertical vertices only
		if p1[1] != p0[1]:
			continue
		middle = ((p1[0] + p0[0]) /2), (p1[1] + p0[1]) /2
		if is_inside(middle[0], middle[1]-0.5):
			vertices[k-1] = (vertices[k-1][0], vertices[k-1][1]+1)
			vertices[k] = (vertices[k][0], vertices[k][1]+1)

	vertices.pop()
	vertices.append(vertices[0])
	print(vertices)

	i_coords = sorted(list(set([ i for (i,_) in vertices ])))
	j_coords = sorted(list(set([ j for (_,j) in vertices ])))
	li = len(i_coords)
	lj = len(j_coords)

	def convert_coord( pos ):
		x, y = pos
		i = i_coords.index(x)
		j = j_coords.index(y)
		return (i, j)

	grid = [ ["." for _ in range(3*(lj-1)+2)] for _ in range(3*(li-1)+2) ]
	mi = 3*(li-1)+2; mj = 3*(lj-1)+2

	for i in range(1, len(vertices)):
		p0, p1 = vertices[i-1], vertices[i]
		c0, c1 = convert_coord(p0), convert_coord(p1)

		ibeg = min(c0[0], c1[0]); iend = max(c0[0], c1[0])
		for i in range(ibeg, iend):
			j = c1[1]
			grid[1+3*i][1+3*j] = "|"
			grid[2+3*i][1+3*j] = "|"
			grid[3+3*i][1+3*j] = "|"
			grid[1+3*i][3*j]   = "|"
			grid[2+3*i][3*j]   = "|"
			grid[3+3*i][3*j]   = "|"

		jbeg = min(c0[1], c1[1]); jend = max(c0[1], c1[1])
		for j in range(jbeg, jend):
			i = c1[0]
			grid[1+3*i][1+3*j] = "="
			grid[1+3*i][2+3*j] = "="
			grid[1+3*i][3+3*j] = "="
			grid[3*i][1+3*j] = "="
			grid[3*i][2+3*j] = "="
			grid[3*i][3+3*j] = "="

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
			if grid[a][b] != ".":
				continue
			grid[a][b] = " "
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
	total = 0
	for i in range(li-1):
		for j in range(lj-1):
			if grid[2+3*i][2+3*j] != " ":
				di = i_coords[i+1] - i_coords[i]
				dj = j_coords[j+1] - j_coords[j]
				total += di * dj

	for line in grid:
		for c in line:
			print(c, end="")
		print()
	print(f"Total: {total}")

input = parse_input("input")
part2(input)

"""
#######
#######
#######
  #####
  #####
#######
#####
#######
 ######
 ######
"""

#  147839462116154