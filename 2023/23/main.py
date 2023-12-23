from collections import defaultdict
from copy import deepcopy
from pprint import pprint
from functools import cache
from graphviz import Digraph
from time import time

dot = Digraph()

class Solver:
	def __init__(self, path="input"):
		self.input = self.parse_input(path)
		self.li = len(self.input)
		self.graph = {}
		self.lj = len(self.input[0])
		self.cache = {}

	def parse_input(self, path):
		with open(path) as file:
			lines = file.read().split("\n")
			return [ [c for c in line] for line in lines ]

	def neighbours(self, position, seen, is_p2):
		i,j=position
		deltas = [(1,0),(-1,0),(0,1),(0,-1)]
		invalid = {(1,0): "^",(-1,0): "v",(0,1): "<",(0,-1): ">"}
		neighs = []
		for (di, dj) in deltas:
			# not in range
			if not (0 <= i+di < self.li and 0 <= j+dj < self.lj):
				continue
			# not in a path / already seen
			if self.input[i+di][j+dj] == "#" or seen[(i+di,j+dj)]:
				continue
			# not in the good direction
			if (not is_p2) and self.input[i+di][j+dj] == invalid[(di,dj)]:
				continue
			neighs.append((i+di, j+dj))
		return neighs

	def get_max_path_from(self, i, j, seen, is_p2):
		if seen == None:
			seen = defaultdict(lambda: False)

		current_length = 0
		position = (i,j)
		while True:
			seen[position] = True
			neighs = self.neighbours(position,seen, is_p2)

			if len(neighs) > 1:
				return current_length + 1 + max([self.get_max_path_from(a,b,deepcopy(seen), is_p2) for (a,b) in neighs])
			
			if len(neighs) == 0:
				return current_length
			
			position = neighs[0]
			current_length += 1

	def p2_neighs(self, position, prec):
		i,j=position
		deltas = [(1,0),(-1,0),(0,1),(0,-1)]
		neighs = []
		for (di, dj) in deltas:
			# not in range
			if not (0 <= i+di < self.li and 0 <= j+dj < self.lj):
				continue
			# not in a path / going back
			if self.input[i+di][j+dj] == "#" or (i+di, j+dj) == prec:
				continue
			neighs.append((i+di, j+dj))
		return neighs

	def find_neighbours(self, edge_pos):
		queue = [(n, edge_pos, 1) for n in self.p2_neighs(edge_pos, edge_pos)]

		while len(queue) != 0:
			(pos, prc, dst) = queue.pop()
			neighs = self.p2_neighs(pos, prc)

			if len(neighs) != 1:
				self.graph[edge_pos].append((dst, pos))
				assert pos in self.graph.keys()
			else:
				queue.append((neighs[0], pos, dst+1))

	def construct_graph(self, i, j):
		self.find_edges((i,j), (i,j))
		self.graph[(i,j)] = []

		for edge_pos in self.graph.keys():
			self.find_neighbours(edge_pos)

	def find_edges(self, start, prec, seen=None):
		if seen == None:
			seen = defaultdict(lambda: False)

		# find edges
		lst = [(start, prec)]
		while len(lst) != 0:
			(pos, prc) = lst.pop()
			if seen[pos]:
				continue

			neighs = self.p2_neighs(pos, prc)
			if len(neighs) != 1:
				self.graph[pos] = []
				seen[pos] = True
				for n in neighs:
					self.find_edges(n, pos, seen)
				break
			lst.append((neighs[0], pos))

	# this should not have worked, it is pure luck as it does not take into account the fact that the walker should end at the bottom tile
	def solve_p1(self):
		print(f"Total: {self.get_max_path_from(0, 1, None, False)}")

	def graph_max_path(self, pos, lasts=(), current_dst=0):
		
		if len(lasts) != 0 and pos == lasts[-1][1]:
			return 0
		
		if pos in [p for _,p in lasts]:
			# we have to remove the last for a certain reason that I totally understand in order to get the right answer
			return current_dst - lasts[-1][0] if lasts[-1][1] == (self.li-1,self.lj-2) else 0

		neighs = self.graph[pos]
		return max([self.graph_max_path(p, lasts + ((dst,pos),) , current_dst+dst) for (dst, p) in neighs])

	def solve_p2(self):
		self.construct_graph(0,1)
		pprint(self.graph)
		print(f"Total: {self.graph_max_path((0,1))}")

	def solve_p2_bis(self):
		self.construct_graph(0,1)
		pprint(self.graph)

	def visu(self):
		self.construct_graph(0,1)
		for k,vls in self.graph.items():
			dot.node(str(k), str(k))
			for (d, n) in vls:
				dot.edge(str(k), str(n), label=str(d))
		dot.render()
solver = Solver("input")
t = time()
solver.solve_p2()
print(time()-t)