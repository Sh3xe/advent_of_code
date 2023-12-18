import re
from math import lcm

seq = []
beg = []
map = {}

def parse_input(path="input2"):
	global sequence, map
	with open(path) as file:
		lines = file.read().split("\n")
		for r in lines[0]:
			if r == "R":
				seq.append(1)
			else:
				seq.append(0)

		for line in lines[1:]:
			if line == "":
				continue
			src, lft, rgt = re.findall("([0-9A-Z]+) = \\(([0-9A-Z]+), ([0-9A-Z]+)\\)", line)[0]
			map[src] = [lft, rgt]
	
	for node in map.keys():
		if node[-1] == "A":
			beg.append(node)

def get_begin():
	paths = []
	for path in map.keys():
		if path[-1] == "A":
			paths.append(path)
	return paths

parse_input("input")

begin = get_begin()
lengths = []
for node in begin:
	k = 0
	while node[-1] != "Z":
		node = map[node][seq[k % len(seq)]]
		k += 1
	lengths.append(k)


prod = 1
for l in lengths:
	prod *= l
print(lengths, prod)
print(lcm(lengths))