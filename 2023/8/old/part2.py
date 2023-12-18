import re

seq = []
map = {}
beg = []

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

def get_path(begin):
	visited = {}
	for key in map.keys():
		visited[key] = (False, -1)

	node = begin
	k = 0
	first_revisit = -1
	t = -1
	z_list = []
	print(node, end=" ")

	while True:
		vis, id = visited[node]
		if vis:
			first_revisit = id 
			t = k - id
			break
		if node[-1] == "Z":
			z_list.append(k)

		visited[node] = (True, k)
		node = map[node][seq[k % len(seq)]]
		k += 1
		print(node, end=" ")
	
	print(first_revisit, t, z_list)



parse_input("input")

for path in map.keys():
	get_path(path)
	assert False