from math import ceil
from functools import cache

infos = []

g_nums = []
g_beg = ""

def unfold_beg(beg, nums):
	new_beg = "?".join( [beg] * 5)
	new_nums = nums * 5
	return new_beg, new_nums

with open("input2", "r") as file:
	lines = file.read().split("\n")
	for line in lines:
		(beg, end) = line.split(" ")
		nums = [int(a) for a in end.split(",")]
		infos.append((beg, nums))

def is_valid(proposal, nums):
	ns = []
	current_count = 0
	for i in range(len(proposal)):
		if proposal[i] == "#":
			current_count += 1
		else:
			if current_count == 0:
				continue
			ns.append(current_count)
			current_count = 0
	if current_count != 0:
		ns.append(current_count)
		current_count = 0
	return ns == nums

@cache
def get_count(bi, ni):
	global g_nums, g_beg
	if bi == 1:
		# default case for bi = 1, for all ni
		return 0
	if ni == 1:
		# default case for ni = 1, for all bi
		return 0

	# recursive case

	for decl in range(bi-ni+1):
		if bi - ni - decl == 0:
			# test if (bi - ni - decl - 1) contains "."
			pass
		
		for j in range(bi-decl):
			# must all be "."
			pass

		pass
	return 0

total = 0
for (beg, nums) in infos:
	nb, nn = unfold_beg(beg, nums)
	g_nums = nn
	g_beg = nb
	get_count.cache_clear()
	total += get_count(len(nb), len(nn))

print("Total: ", total)