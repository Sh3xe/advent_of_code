import re

card_pts = []
card_nb = []
with open("input") as f:
	lines = f.read().split("\n")
	for line in lines:
		parts = line.split("|")
		if len(parts) != 2:
			continue
		winning = [ int(num) for num in re.findall("[0-9]+", parts[0])][1:]
		pick = [ int(num) for num in re.findall("[0-9]+", parts[1])]

		points = 0
		pt = 0
		for p in pick:
			if p in winning:
				pt += 1
				if points == 0:
					points = 1
				else:
					points *= 2
		card_pts.append(points)
		card_nb.append(pt)


copies_earns = [0] * len(card_pts)

for i in range(len(card_pts)):
	points = card_nb[i]
	#print("CARD", i, points, copies_earns[i])
	copies_earns[i] += 1
	for j in range(points):
		if i+j+1 < len(card_pts):
			#print(copies_earns[i], i+j+1)
			copies_earns[i+j+1] += 1 * copies_earns[i]
	#print(copies_earns)

#print(copies_earns, card_pts)
print(sum(copies_earns))