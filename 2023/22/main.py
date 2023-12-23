from copy import deepcopy

def parse_input(path="ex"):
	bricks = []
	with open(path) as file:
		line = file.readline()
		while line:
			beg, end = line.split("~")
			p0 = [int(i) for i in beg.split(",")]
			p1 = [int(i) for i in end.split(",")]
			bricks.append((p0, p1))
			line = file.readline()
	return bricks

def part1(brks):
	bricks = brks.copy()
	support_data = {}

	def projection_collide(p0, p1, q0, q1):
		return p1[1]>=q0[1] and p0[1]<=q1[1] and p1[0]>=q0[0] and p0[0]<=q1[0]

	def calculate_gravity():
		# make the bricks fall
		for i in range(len(bricks)):
			support_data[i] = {"sup": [], "sup_by": []}
			p0, p1 = bricks[i]
			min_delta_z = p0[2]-1
			for j in range(i):
				q0,q1 = bricks[j]
				if p0[2] <= q1[2]:
					continue
				if projection_collide(p0,p1,q0,q1):
					min_delta_z = min(min_delta_z, p0[2] - q1[2] - 1)
			
			bricks[i][0][2] -= min_delta_z
			bricks[i][1][2] -= min_delta_z

	def calculate_supports():
		# calculate which brick supports which
		for i in range(len(bricks)):
			p0, p1 = bricks[i]
			for j in range(i):
				q0,q1 = bricks[j]
				if projection_collide(p0,p1,q0,q1) and q1[2] == p0[2]-1:
					support_data[i]["sup_by"].append(j)
					support_data[j]["sup"].append(i)

	def calculate_num_falls(i):
		data = deepcopy(support_data)
		level = [i]
		removed = []

		while len(level) != 0:
			for k in level:
				for d in data.values():
					if k in d["sup_by"]:
						d["sup_by"].remove(k)
				removed.append(k)

			level = []
			
			for k in range(len(bricks)):
				if bricks[k][0][2] == 1: # is on the ground
					continue
				if k in removed: # do not exist at this point
					continue
				if len(data[k]["sup_by"]) == 0: # not supported by anything, remove it
					level.insert(0, k)

		return len(removed) - 1

	calculate_gravity()
	calculate_supports()
	total = sum([calculate_num_falls(i) for i in range(len(bricks))])
	print(f"Total: {total}")

bricks = parse_input("input")
bricks.sort(key=lambda t:t[0][2] )
part1(bricks)