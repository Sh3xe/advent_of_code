import re

sequence = ""
map = {}

with open("input") as file:
	lines = file.read().split("\n")
	sequence = lines[0]

	for line in lines[1:]:
		if line == "":
			continue
		src, lft, rgt = re.findall("([0-9A-Z]+) = \\(([0-9A-Z]+), ([0-9A-Z]+)\\)", line)[0]
		map[src] = [lft, rgt]
	
current_nodes = []

for node in map.keys():
	if node[-1] == "A":
		current_nodes.append(node)

steps = 0
done = False
while not done:
	if sequence[steps % len(sequence)] == "R":
		id = 1
	else:
		id = 0
	
	for i in range(len(current_nodes)):
		current_nodes[i] = map[current_nodes[i]][id]
	steps += 1

	done = True
	for node in current_nodes:
		if node[-1] != "Z":
			done = False

print(steps)