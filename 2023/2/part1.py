import re

def get_game_picks(path="input"):
	picks = []
	with open(path) as file:
		while True:
			line = file.readline()
			if not line:
				break
			
			matches = re.findall("([0-9]*) (red|green|blue)(,|;|$)?", line)
			line_picks = []
			current_pick = []
			for (num, col, sep) in matches:
				assert int(num) >= 0
				current_pick.append( (int(num), col) )
				if sep != ",":
					line_picks.append(current_pick)
					current_pick = []

			picks.append(line_picks)
	return picks
				
def is_pick_possible(pick, bag_content):
	for (num, col) in pick:
		if bag_content[col] < num:
			return False
	return True

def minimum_set(game):
	min_set = {"red": 0, "green": 0, "blue": 0}
	for picks in game:
		for (num,col) in picks:
			min_set[col] = max(num, min_set[col])
	return min_set

game_picks = get_game_picks()
power_sum = 0
for game in game_picks:
	mini_set = minimum_set(game)
	power_sum += mini_set["red"] * mini_set["green"] * mini_set["blue"]
print(power_sum)

# BAG_CONTENT = {
# 	"red": 12,
# 	"green": 13,
# 	"blue": 14
# }

# game_picks = get_game_picks()
# id_sum = 0
# for i in range(len(game_picks)):
# 	picks = game_picks[i]
# 	possible = True
# 	for pick in picks:
# 		possible &= is_pick_possible(pick, BAG_CONTENT)
# 	if possible:
# 		id_sum += i + 1

# print(id_sum)