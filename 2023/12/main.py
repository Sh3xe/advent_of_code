from functools import cache

def parse_input(path):
	lines = open(path).read().split("\n")
	splits = [line.split(" ") for line in lines]
	values = [(beg, list(map(int, end.split(",")))) for (beg, end) in splits ]
	return [ ("?".join( [sp]*5 ), nm*5) for (sp, nm) in values]

@cache
def count(spring, nums, sp_len, nm_len):
	if nm_len == 0:
		return all([spring[i] != "#" for i in range(sp_len)])
	current_num = nums[nm_len-1]
	if sp_len < current_num:
		return 0
	s = 0
	for offset in range(0, sp_len-current_num+1):
		ok = all([ spring[after] != "#" for after in range(sp_len-offset, sp_len)])
		ok &= all([spring[i] != "." for i in range(sp_len-offset-current_num, sp_len-offset)])
		if sp_len-current_num-offset != 0:
			ok &= (spring[sp_len-current_num-offset-1] != "#")
		if ok:
			s += count(spring, nums, sp_len-current_num-offset-1,nm_len-1)
	return s

springs = parse_input("input")

s = sum([count( tuple(sp), tuple(nm), len(sp), len(nm) ) for (sp, nm) in springs])
print("Total: ", s)