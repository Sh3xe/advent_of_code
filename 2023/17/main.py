import heapq
from collections import defaultdict


def parse_input(path="test_input"):
	return [ [int(i) for i in line] for line in open(path).read().split("\n")]

def print_input(input, path):
	path = [ p[0] for p in path ]

	print("+", end="")
	print("-" * (len(input[0])), end="")
	print("+")
	for i, line in enumerate(input):
		print("|",end="")
		for j,c in enumerate(line):
			if (i,j) in path:
				print(" ", end="")
			else:
				print(c, end="")
		print("|", end="\n")
	print("+", end="")
	print("-" * (len(input[0])), end="")
	print("+")

def construct_path(last_dict, pos):
	path = []
	current = pos
	while current[0] != (0, 0):
		path.append(current)
		current = last_dict[current]
	return list(reversed(path))

def p1_nei(state, li, lj):
	pos, delta, dst = state
	dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
	neis = []
	for d in dirs:
		if d[0] == -delta[0] and d[1] == -delta[1]:
			continue
		if not (0 <= pos[0] + d[0] < li) or not (0 <= pos[1] + d[1] < lj):
			continue
		new_dst = 1 if d != delta else dst+1
		if new_dst > 3:
			continue
		neis.append( ((pos[0] + d[0], pos[1] + d[1]), d, new_dst) )
	return neis
	
def p2_nei(state, li, lj):
	pos, delta, dst = state
	dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
	neis = []
	for d in dirs:
		if d[0] == -delta[0] and d[1] == -delta[1]:
			continue
		if not (0 <= pos[0] + d[0] < li) or not (0 <= pos[1] + d[1] < lj):
			continue
		new_dst = 1 if d != delta else dst+1
		if new_dst > 10:
			continue
		if d != delta and delta != (0, 0) and dst < 4:
			continue
		neis.append( ((pos[0] + d[0], pos[1] + d[1]), d, new_dst) )
	return neis

def day17(input, neighs):
	lj = len(input[0])
	li = len(input)
	length = defaultdict(lambda: 99999999)
	last = {}

	def wheight(state):
		pos, _, _ = state
		return input[pos[0]][pos[1]]

	def sort_key(state):
		pos, _, _ = state
		return length[state] + (li-1-pos[0]) + (lj-1-pos[1])
	
	s0 = ((0,0),(0,0),1)
	end_state = ()
	length[((0,0),(0,0),1)] = input[0][0]
	heap = [(sort_key(s0), s0)]

	while len(heap) != 0:
		(_, cstate) = heapq.heappop(heap)

		if cstate[0] == (li-1,lj-1) and cstate[2] >= 4:
			end_state = cstate
			break

		for nei in neighs(cstate, li, lj):
			current_len = length[cstate] + wheight(nei)
			if current_len >= length[nei]:
				continue
			length[nei] = current_len
			last[nei] = cstate
			heapq.heappush(heap, (sort_key(nei), nei))

	#print(dict(length), dict(last))
	path = construct_path(last, end_state)
	print_input(input, path)
	total = sum([input[pos[0]][pos[1]] for (pos,_,_) in path])
	print(f"Total: {total}")

input = parse_input("input")
#day17(input, p1_nei)
day17(input, p2_nei)

"""
def day17(input, neighs):
	lj = len(input[0])
	li = len(input)
	length = defaultdict(lambda: 99999999)
	last = {}

	def wheight(state):
		pos, _, _ = state
		return input[pos[0]][pos[1]]

	def sort_key(state):
		pos, _, _ = state
		return length[state] + (li-1-pos[0]) + (lj-1-pos[1])
	
	queue = [((0,0),(0,0),1)]
	length[((0,0),(0,0),1)] = input[0][0]
	end_state = ()

	while len(queue) != 0:
		cstate = queue.pop()

		if cstate[0] == (li-1,lj-1):
			end_state = cstate
			break

		for nei in neighs(cstate, li, lj):
			current_len = length[cstate] + wheight(nei)
			if current_len >= length[nei]:
				continue
			length[nei] = current_len
			last[nei] = cstate
			queue.append(nei)

		queue.sort(reverse=True, key=sort_key)

	#print(dict(length), dict(last))
	path = construct_path(last, end_state)
	print_input(input, path)
	total = sum([input[pos[0]][pos[1]] for (pos,_,_) in path])
	print(f"Total: {total}")
"""