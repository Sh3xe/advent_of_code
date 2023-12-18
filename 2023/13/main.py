
patterns = []
lines = open("input").read().split("\n")
current_pattern = []
for line in lines:
	if line == "":
		patterns.append(current_pattern)
		current_pattern = []
	else:
		current_pattern.append(line)

def get_hori(pat):
	indices = []
	for i in range(len(pat)):
		not_refl_count = 0
		for j in range(99999):
			if i+j+1 >= len(pat) or i-j < 0:
				break
			if pat[i+j+1] != pat[i-j]:
				for k in range(len(pat[0])):
					if pat[i+j+1][k] != pat[i-j][k]:
						not_refl_count += 1
		if not_refl_count == 1:
			indices.append(i)
	return [i+1 for i in indices]

def get_vert(pat):
	indices = []
	for i in range(len(pat[0])):
		not_refl_count = 0
		for j in range(99999):
			if i+j+1 >= len(pat[0]) or i-j < 0:
				break
			for k in range(len(pat)):
				if pat[k][i-j] != pat[k][j+i+1]:
					not_refl_count += 1
		if not_refl_count == 1:
			indices.append(i)
	return [i+1 for i in indices]

s = 0
for pattern in patterns:
	#print(get_vert(pattern))
	s += sum(get_hori(pattern)) * 100
	s += sum(get_vert(pattern))

print("Total: ", s)