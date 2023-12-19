import re

def get_letter(l):
	return "xmas".index(l)

def parse_input(path):
	lines = open(path).read().split("\n")
	workflows = {}
	i = 0
	while True:
		if lines[i] == "":
			i += 1
			break

		line = lines[i]
		splt = line.split("{")
		steps = splt[1][:-1].split(",")
		workflows[splt[0]] = steps
		i += 1

	objects = []
	for line in lines[i:]:
		m = re.findall("{x=(\\d+),m=(\\d+),a=(\\d+),s=(\\d+)}", line)[0]
		objects.append( (int(m[0]), int(m[1]), int(m[2]), int(m[3])) )

	return workflows, objects

def part1(workflows, objects):
	def is_accepted(obj):
		current = "in"
		while True:
			steps = workflows[current]
			for step in steps:
				if "<" in step or ">" in step:
					member, cmp, value, jmp = re.findall("([a-z])(<|>)(\\d+):(A|R|[a-z]+)", step)[0]
					value = int(value)
					val = obj[get_letter(member)]
					if (cmp == ">" and val > value) or (cmp == "<" and val < value):
						if jmp == "A":
							return True
						elif jmp == "R":
							return False
						else:
							current = jmp
							break
				elif step == "A":
					return True
				elif step == "R":
					return False
				else:
					current = step

	s = 0
	for obj in objects:
		if is_accepted(obj):
			s += sum(obj)

	print(f"Total: {s}")

# returns (new_ranges, next) with next = "R|A|next" or "N" if the range was not explicitly rejected (i.e, it should be treated still)
def split_with_step(ranges, step):
	matches = re.findall("([a-z])(<|>)(\\d+):(A|R|[a-z]+)", step)
	if len(matches) != 0:
		member, op, value, next = matches[0]
		value = int(value)
		id = get_letter(member)
		(beg, end) = ranges[id]
		if op == ">":
			if end <= value:
				return [(ranges, "N")]
			elif beg > value:
				return [(ranges, next)]
			else:
				r0 = list(ranges)
				r0[id] = (beg, value)
				r1 = list(ranges)
				r1[id] = (value+1, end)
				return [(tuple(r0), "N"), (tuple(r1), next)]
		if op == "<":
			if beg >= value:
				return [(ranges, "N")]
			elif end < value:
				return [(ranges, next)]
			else:
				r0 = list(ranges)
				r0[id] = (beg, value-1)
				r1 = list(ranges)
				r1[id] = (value, end)
				return [(tuple(r0), next), (tuple(r1), "N")]
	elif step == "R":
		return [(ranges, "R")]
	elif step == "A":
		return [(ranges, "A")]
	else:
		return [(ranges, step)]

def split_range(ranges, steps):
	next_ranges = []
	current_ranges = [ranges]
	for step in steps:
		arr = current_ranges.copy()
		current_ranges = []
		for r in arr:
			for new_r, next in split_with_step(r, step):
				if next == "N":
					current_ranges.append(new_r)
				else:
					next_ranges.append((new_r, next))
	return next_ranges

def part2(workflows):
	START_RANGE = ((1, 4000), (1, 4000), (1, 4000), (1, 4000))
	accepted_ranges = []
	to_be_processed = [(START_RANGE, "in")]
	while len(to_be_processed) != 0:
		ranges,start = to_be_processed.pop()

		for (new_ranges, next) in split_range(ranges, workflows[start]):
			if next == "A":
				accepted_ranges.append(new_ranges)
			elif next != "R":
				to_be_processed.append((new_ranges, next))

	total = 0
	for x, m, a, s in accepted_ranges:
		total += (x[1]-x[0]+1)*(m[1]-m[0]+1)*(a[1]-a[0]+1)*(s[1]-s[0]+1)

	print(f"Total: {total}")

workflows, objects = parse_input("test_input.txt")
part2(workflows)