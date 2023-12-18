import re 

def parse_input(path):
	with open(path) as file:
		return file.read().split(",")

def elf_hash(str):
	s = 0
	for c in str:
		s += ord(c)
		s *= 17
		s = s % 256
	return s

def calculate_box_data(steps):
	box_data = [[] for _ in range(256)]

	for step in steps:
		(label, operator, value) = re.findall("([a-z]*)(=|-)([1-9]?)", step)[0]
		id = elf_hash(label)
		if operator == "-":
			box_data[id] = list(filter(lambda tpl: tpl[0] != label, box_data[id]))
		else:
			try:
				idd = [i for i, (l, _) in enumerate(box_data[id]) if l == label][0]
				box_data[id][idd] = (label, int(value))
			except IndexError:
				box_data[id].append((label, int(value)))
	return box_data

def calculate_focusing_power(box_data):
	total = 0
	for i, box in enumerate(box_data):
		for j, (_, val) in enumerate(box):
			total += (i+1) * (j+1) * val
	return total

steps = parse_input("input")
box_data = calculate_box_data(steps)
print(f"Total: {calculate_focusing_power(box_data)}")