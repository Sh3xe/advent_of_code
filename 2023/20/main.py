from collections import defaultdict
#from graphviz import Digraph

#dot = Digraph()
#dot.edges(['AB', 'AB', 'AB', 'BC', 'BA', 'CB'])

def parse_input(path="input_test.txt"):
	obj = defaultdict(lambda: {"type": "o", "data": False})
	
	for line in open(path).read().split("\n"):
		if line == "":
			continue
		a, b = line.split("->")
		a = a.rstrip().lstrip()
		b = [el.rstrip().lstrip() for el in b.rstrip().lstrip().split(",")]
		#dot.node(a[1:], a)
		#for el in b:
		#	dot.edge(a[1:], el)
		if "broadcaster" in a:
			obj["broadcaster"] = {
				"connections": b,
				"type": "b"
			}
		elif a[0] == "%":
			obj[a[1:].rstrip()] = {
				"data": False,
				"connections": b,
				"type": "%"
			}
		elif a[0] == "&":
			obj[a[1:].rstrip()] = {
				"type": "&",
				"connections": b,
				"data": defaultdict(lambda: False)
			}

	obj["output"] = {
		"type": "o",
		"data": False,
		"connections": []
	}

	t = list(obj.items())
	for (key, value) in t:
		vs = value["connections"]
		for conn in vs:
			if obj[conn]["type"] == "&":
				obj[conn]["data"][key] = False

	return obj

def part1(input):
	counts = [0,0]
	def send(signal, name, log=False):
		signals = [(name, signal, "button")]
		
		while len(signals) != 0:
			(nme, sig, pre) = signals.pop()
			obj = input[nme]

			counts[sig] += 1
			if log:
				t = ["low", "high"][sig]
				print(f"{pre} -{t}-> {nme}")
			
			if obj["type"] == "b":
				for conn in obj["connections"]:
					signals.insert(0, (conn, sig, nme) )
			elif obj["type"] == "%":
				if sig == True:
					continue
				obj["data"] = not obj["data"]
				for conn in obj["connections"]:
					signals.insert(0, (conn, obj["data"], nme) )
			elif obj["type"] == "&":
				obj["data"][pre] = sig
				val = not all(obj["data"].values())
				for conn in obj["connections"]:
					signals.insert(0, (conn, val, nme) )
			elif obj["type"] == "o":
				obj["data"] = sig

	for _ in range(1000):
		send(False, "broadcaster")

	print(f"Total: {(counts[0])*(counts[1])}, with {counts}")

input = parse_input("input.txt")
part1(input)
#dot.render(view=True)


"""
PART2:
	there is no part 2 because it was done with pen and paper
"""