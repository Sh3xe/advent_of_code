#include <fstream>
#include <map>
#include <vector>

int main()
{
	std::string sequence;
	std::map<std::string, std::pair<std::string, std::string> > map;

	std::fstream file {"input2"};

	file >> sequence;
	std::string line;
	while( std::readline())

	for line in lines[1:]:
		if line == "":
			continue
		src, lft, rgt = re.findall("([0-9A-Z]+) = \\(([0-9A-Z]+), ([0-9A-Z]+)\\)", line)[0]
		map[src] = [lft, rgt]
	file.close();

	return 0;
}

/*
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

print(steps)*/