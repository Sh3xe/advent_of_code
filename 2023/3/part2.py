
lines = []
valid_map = []
size_i = 0
size_j = 0

def print_sche():
	for i in range(size_i):
		for j in range(size_j):
			if valid_map[i][j]:
				print("#", end="")
			else:
				print(" ", end="")
		print()

def get_schematic(path="input"):
	global lines, valid_map, size_i, size_j
	with open(path, "r") as file:
		while True:
			line = file.readline()
			if not line:
				break
			line = line.strip()
			lines.append(line)
			valid_map.append( [False] * len(line) )
	(size_i, size_j) = len(lines), len(lines[0])
	return (lines, valid_map)

def propagate_validity(i, j):
	global lines, valid_map, size_i, size_j
	# for each 2D-neighbours
	for irel in range(-1, 2):
		for jrel in range(-1, 2):
			# out of range or, continue
			if not( 0 <= i+irel < size_i and 0 <= j+jrel < size_j ):
				continue
			# if it is a number
			if lines[i+irel][j+jrel] in "0123456789":
				# propagate
				k = j+jrel
				while k < size_j:
					if lines[i+irel][k] in "0123456789":
						valid_map[i+irel][k] = True
					else:
						break
					k += 1
				k = j+jrel
				while k >= 0:
					if lines[i+irel][k] in "0123456789":
						valid_map[i+irel][k] = True
					else:
						break
					k -= 1
	
def get_neighbouring_stars(i, j):
	global lines, valid_map, size_i, size_j
	neighbouring_stars = []
	# for each 2D-neighbours
	for irel in range(-1, 2):
		for jrel in range(-1, 2):
			# out of range or, continue
			if not( 0 <= i+irel < size_i and 0 <= j+jrel < size_j ):
				continue
			if lines[i+irel][j+jrel] == "*":
				neighbouring_stars.append((i+irel, j+jrel))
	return neighbouring_stars

schematic = get_schematic()
lines, valid_map = schematic
(size_i, size_j) = len(lines), len(lines[0])
for i in range(size_i):
	for j in range(size_j):
		if lines[i][j] not in "0123456789.":
			propagate_validity(i, j)

valid_numbers = []
gear_dict = {}

for i in range(size_i):
	current_number = ""
	neighbouring_stars = []
	for j in range(size_j):
		c = lines[i][j]
		if c in "0123456789" and valid_map[i][j]:
			current_number += c
			l = get_neighbouring_stars(i, j)
			neighbouring_stars.extend( l )
		else:
			if current_number != "":
				valid_numbers.append(int(current_number))
				for (si, sj) in list(set(neighbouring_stars)):
					key = "{}, {}".format(si,sj)
					try:
						gear_dict[key].append(int(current_number))
					except:
						gear_dict[key] = [int(current_number)]

			current_number = ""
			neighbouring_stars = []
	if current_number != "":
		valid_numbers.append(int(current_number))
		for (si, sj) in list(set(neighbouring_stars)):
			key = "{}, {}".format(si,sj)
			try:
				gear_dict[key].append(int(current_number))
			except:
				gear_dict[key] = [int(current_number)]

res = 0
for (key, lst) in gear_dict.items():
	if len(lst) == 2:
		res += lst[0] * lst[1]
print(res)