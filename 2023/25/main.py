from pprint import pprint
from collections import defaultdict
from graphviz import Graph

def parse_input(path="ex"):
	d = {}
	with open(path) as file:
		for line in file.read().split("\n"):
			splt = line.split(" ")
			if splt[0][:-1] == "slz":
				print(splt)
			d[splt[0][:-1]] = splt[1:]
	return d

def list_keys(input):
	l = list(input.keys())
	for val in input.values():
		l.extend(val)
	l.sort()
	return sorted(list( set(l) ))

def create_matrix_rep(input):
	keys = list_keys(input)
	line = [ False for _ in range(len(keys)) ]
	matrix = [ line.copy() for _ in range(len(keys))]

	for i in range(len(keys)):
		for j in range(len(keys)):
			neighs_i = input.get(keys[i])
			neighs_j = input.get(keys[j])
			
			if neighs_i != None:
				if keys[j] in neighs_i:
					matrix[i][j] = True
					matrix[j][i] = True
			elif neighs_j != None:
				if keys[i] in neighs_j:
					matrix[i][j] = True
					matrix[j][i] = True

	return keys, matrix

def print_matrix_rep(mat):
	for l in mat:
		for i in l:
			print(1 if i else 0, end="")
		print()

def export_pdf(path):
	dot = Graph()
	keys, mat = create_matrix_rep(parse_input(path))
	for key in keys:
		dot.node(key, key)
	
	for i in range(len(mat)):
		for j in range(i+1, len(mat)):
			if mat[i][j]:
				dot.edge(keys[i], keys[j], str(i)+"-"+str(j))
	
	dot.render(view=True)

def part1(input):
	"""
	solved visually:
		kcn-slz
		lzd-fbd
		ptq-fxn
	"""
	
	def remove_edge(a,b):
		try:
			input[a].remove(b)
		except:
			input[b].remove(a)

	remove_edge("lzd", "fbd")
	remove_edge("ptq", "fxn")
	remove_edge("kcn", "szl")

	keys = list(input.keys())
	for el in keys:
		l = input[el]
		for v in l:
			try:
				input[v].append(el)
			except:
				input[v] = [el]

	keys = list_keys(input)
	size = 0
	seen = defaultdict(lambda: False)
	lst = [keys[0]]
	while(len(lst)) != 0:
		el = lst.pop()
		if seen[el]:
			continue
		seen[el] = True
		lst.extend(input[el])
		size += 1

	print(f"Total: {size*(len(keys)-size)}")
	print(size, len(keys))


input = parse_input("input")
part1(input)