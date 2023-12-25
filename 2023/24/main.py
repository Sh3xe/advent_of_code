
def parse_input(path="ex"):
	input = []
	with open(path) as file:
		lines = file.read().split("\n")
		for line in lines:
			(beg,end,) = line.split("@")
			pos = tuple(int(n) for n in beg.split(","))
			vel = tuple(int(n) for n in end.split(","))
			input.append((pos,vel))
	return input

# cf. math
def intersect(p0, v0, p1, v1):
	det = -v0[1]*v1[0] + v0[0]*v1[1]
	if det == 0: return None

	x0 = [v0[0]*p0[1]-v0[1]*p0[0], v1[0]*p1[1]-v1[1]*p1[0]]
	p = [v1[0]*x0[0]-v0[0]*x0[1], v1[1]*x0[0]-v0[1]*x0[1]]
	p[0] /= det; p[1] /= det

	d1 = (p[0]-p0[0])*v0[0] + (p[1]-p0[1])*v0[1]
	d2 = (p[0]-p1[0])*v1[0] + (p[1]-p1[1])*v1[1]
	return p if d1 > 0 and d2 > 0 else None

def count_intersection(input, pmin, pmax):
	count = 0
	for i in range(len(input)):
		p0, v0 = input[i]
		for j in range(i+1, len(input)):
			p1, v1 = input[j]
			inter = intersect(p0, v0, p1, v1)
			if inter != None and pmin <= inter[0] <= pmax and pmin <= inter[1] <= pmax:
				count += 1
	return count

def t_to_coeff(p,v):
	"""
	given a line as {p+vt/for all t} = line, 
	returns (a,b,c), r so that
	line = {x,y,z / ax +by +cz = r }
	"""
	n = (0, v[2], -v[1])
	r = sum(p[i]*n[i] for i in range(3))
	return n, r

def resolve_sys(l1,l2,l3):
	"""
	resolve the system given by l1..l3:
	xli0 + yli1 + zli2 = li3 for all i from 1 to 3
	"""

input = parse_input("input")
resolve_sys()
#print(f"Total: {count_intersection(input, 200000000000000, 400000000000000)}")
