from copy import deepcopy

def parse_input(path="ex.txt"):
	lines = open(path).read().split("\n")
	return [ [c for c in l] for l in lines]

def part1(input):
	li, lj = len(input), len(input[0])

	def neighs(i, j, input):
		ns = []
		for (di, dj) in [(1,0), (-1,0), (0,1), (0,-1)]:
			if 0 <= i+di < li and 0 <= j+dj < lj and input[i+di][j+dj] != "#":
				ns.append((i+di, j+dj))
		return ns

	def calc_next(input):
		cpy = deepcopy(input)
		positions = []
		for i in range(li):
			for j in range(lj):
				if input[i][j] in "OS":
					positions.append((i,j))
					cpy[i][j] = "."
		
		for (i,j) in positions:
			for (a,b) in neighs(i,j,input):
				cpy[a][b] = "O"
		return cpy

	for _ in range(65+65):
		input = calc_next( input )
		for l in input:
			print("".join(l))
		print()
	
	total = 0
	for i in range(li):
		for j in range(lj):
			print(input[i][j], end="")
			total += input[i][j] in "O"
		print()
	print(f"Total: {total}")	

def get_res(input, start, nm):
	li, lj = len(input), len(input[0])
	input[65][65] = "."
	for s0 in start:
		input[s0[0]][s0[1]] = "S"

	def neighs(i, j, input):
		ns = []
		for (di, dj) in [(1,0), (-1,0), (0,1), (0,-1)]:
			if 0 <= i+di < li and 0 <= j+dj < lj and input[i+di][j+dj] != "#":
				ns.append((i+di, j+dj))
		return ns

	def calc_next(input):
		cpy = deepcopy(input)
		positions = []
		for i in range(li):
			for j in range(lj):
				if input[i][j] in "OS":
					positions.append((i,j))
					cpy[i][j] = "."
		
		for (i,j) in positions:
			for (a,b) in neighs(i,j,input):
				cpy[a][b] = "O"
		return cpy

	def calc_total(input):
		total = 0
		for i in range(li):
			for j in range(lj):
				total += input[i][j] in "O"
		return total

	for _ in range(nm):
		input = calc_next( input )
	
	return calc_total(input)

def part2():
	values = [7265,7325]
	step_count = 26501365

	total = 0

	# ist step: special case for the center garden
	total += values[(step_count+1)%2]
	print(f"val:{total}")
	step_count -= 65
	num_gardens = 4
	while step_count != 131:
		step_count -= 131
		total += num_gardens*values[(step_count)%2]
		num_gardens += 4
	print(num_gardens)
	return total

STEPS = 26501365
input = parse_input("input.txt")
total = part2()

vals0 = [[(0,65)], [(65,0)], [(130,65)], [(65,130)]]
vals1 = [[(0,0)], [(130,0)], [(130,130)], [(0,130)]]
for start in vals0:
	v = get_res(deepcopy(input), start, 131)
	print(v, start)
	total += v

for start in vals1:
	v = get_res(deepcopy(input), start, 131*2-65)
	print(v, start)
	total += (((STEPS-65)//131)-1)*v
	print(((STEPS-65)//131))

print(total)
# 597 117 936 063 807: too high
# 597 100 065 069 222: too low
# 597 100 065 069 162: too low

# 597 102 249 291 465: non
# 597 100 040 793 162: non