from random import randint
from collections import defaultdict

def parse_input(path):
	lines = []
	with open(path) as file:
		lines = file.read().splitlines()
	return lines

def rotate(lines):
	dirs = [(1, 0, 0, 0, -1, 0), (0, 0, 1, 0, 0, -1), (0, 1, 0, 0, 1, 0), (0, 0, 0, 1, 0, 1)]
	lines = [list(l) for l in lines]
	for (a, b, c, d, di, dj) in dirs:
		change = True
		while change:
			lns = lines.copy()
			change = False
			for i in range(a, len(lns)-b):
				for j in range(c,len(lns[0])-d):
					if lines[i+di][j+dj] == "." and lines[i][j] == "O":
						lns[i+di][j+dj] = "O"
						lns[i][j] = "."
						change = True
			lines = lns
	return ["".join(l) for l in lines]

def get_tot(lines):
	total = 0
	for i in range(len(lines)):
			for j in range(len(lines[0])):
				if lines[i][j] == "O":
					total += len(lines) - i
	return total

def generate_random(length, rock_count, wall_count):
	lines = [["."]*length for _ in range(length)]
	for _ in range(rock_count):
		vals = [randint(0, length-1) for _ in range(2)]
		for _ in range(4):
			vals.append(randint(0, length-1))
		lines[vals[0]][vals[1]] = "O"
	for _ in range(wall_count):
		vals = [randint(0, length-1) for _ in range(2)]
		lines[vals[0]][vals[1]] = "#"
	return ["".join(l) for l in lines]

def print_lines(lines):
	for l in lines:
		print(l)
	print()

def get_n_th(state, n):
	states = defaultdict(lambda :-1)
	i = 0
	loop_begin = -1
	totals = []
	while True:
		state = rotate(state)
		state_hash = hash(tuple(state))
		if states[state_hash] != -1:
			loop_begin = states[state_hash]
			break
		states[state_hash] = i
		totals.append(get_tot(state))
		i += 1

	loop_size = i - loop_begin
	c = n - loop_begin - 1
	return totals[loop_begin+(c % loop_size)]

print(get_n_th(parse_input("input2"), 1_000_000_000))