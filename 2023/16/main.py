
out = open("out.txt", "w")

def parse_input(path="input2"):
	return list( filter(lambda l: len(l) != 0, open(path).read().split("\n") ) )

def print_input(input, seen):
	for i in range(len(input)):
		for j in range(len(input[0])):
			if any(seen[i][j]):
				out.write("#")
			else:
				out.write(input[i][j])
		out.write("\n")
	out.write("\n")

def part1(input, spos, sdir):
	def dir_to_id(dir):
		if dir == (0, 1):
			return 0
		if dir == (0, -1):
			return 1
		if dir == (-1, 0):
			return 2
		if dir == (1, 0):
			return 3

	seen = [ [] for _ in range(len(input)) ]
	for i in range(len(seen)):
		seen[i] = [ [False, False, False, False] for _ in range(len(input[0]))]

	beams = [(spos, sdir)]

	while len(beams) != 0:
		pos, dir = beams.pop()
		#print_input(input, seen)

		# cas particulier de merde
		if pos[1] != -1 and pos[0] != -1 and pos[1] != len(input) and pos[0] != len(input[0]):
			# already been here
			if seen[pos[0]][pos[1]][dir_to_id(dir)]:
				continue
			seen[pos[0]][pos[1]][dir_to_id(dir)] = True
		
		# next position is out of bound
		if not (0 <= pos[0] + dir[0] < len(input)) or not ( 0 <= pos[1] + dir[1] < len(input[0]) ):
			continue

		c = input[pos[0]+dir[0]][pos[1]+dir[1]]
		npos = (pos[0]+dir[0], pos[1]+dir[1])
		if c == "|" and dir[0] == 0:
				beams.append( (npos , (1,0)) )
				beams.append( (npos , (-1,0)) )
		elif c == "-" and dir[1] == 0:
				beams.append( (npos , (0,1)) )
				beams.append( (npos , (0,-1)) )
		elif c == "\\":
				beams.append( (npos , (dir[1], dir[0])) )
		elif c == "/":
				beams.append( (npos , (-dir[1], -dir[0])) )
		else:
			beams.append( (npos , dir) )

	print_input(input, seen)
	
	c= 0
	for i in range(len(input)):
		for j in range(len(input[0])):
			if any(seen[i][j]):
				c += 1
	return c


input = parse_input("input")
m = 0
for i in range(len(input)):
	m = max(part1(input, (i, -1), (0, 1)), m)
	m = max(part1(input, (i, len(input[0])), (0, -1)), m)

for j in range(len(input[0])):
	m = max(part1(input, (-1, j), (1, 0)), m)
	m = max(part1(input, (len(input), j), (-1, 0)), m)

print(m)