import re

PATTERN = "(\d) (red|green|blue)"

def get_games( file_name ):
	file = open(file_name)
	games = []
	for line in file.read().split("/n"):
		numbers = re.findall(PATTERN, line)
		games.append( [(int(num), col) for (num, col) in numbers] )
	
	return games

def is_game_possible(game, data):
	pass

games = get_games("input")