import re
import functools

card_data = []

ORDER = {
	"A": 12,
	"K": 11,
	"Q": 10,
	"T": 8,
	"9": 7,
	"8": 6,
	"7": 5,
	"6": 4,
	"5": 3,
	"4": 2,
	"3": 1,
	"2": 0,
	"J": -1
}

def card_cmp(a, b):
	(ta, _, la) = a
	(tb, _, lb) = b 
	if ta > tb:
		return 1
	if ta < tb:
		return -1
	
	for i in range(len(la)):
		if ORDER[la[i]] > ORDER[lb[i]]:
			return 1
		if ORDER[la[i]] < ORDER[lb[i]]:
			return -1

	return 0
	
def get_type(card_dict):
	vals = sorted( [val for val in card_dict.values()] )
	m = max(vals)

	pairs = 0
	for v in vals:
		if v == 2:
			pairs += 1
		
	if m == 1:
		return 0
	if m == 5:
		return 100
	if m == 4:
		return 90
	if m == 2:
		if pairs == 1:
			return 10
		else:
			return 20
	if m == 3:
		if pairs == 1:
			return 50
		else:
			return 40

def get_new_type(card_str):
	(tmax, letter) = (0, "J")

	for l in "AKQT98765432":
		new_card = card_str.replace("J", l)
		card_dict = {}
		for letter in new_card:
			try:
				card_dict[letter] += 1
			except:
				card_dict[letter] = 1
		t = get_type(card_dict)
		if t >= tmax:
			(tmax, letter) = (t, l)
	
	return tmax


with open("input") as file:
	for line in file.read().split("\n"):
		if line == "":
			continue
		[letters, bid] = line.split(" ")
		# card_dict = {}
		# for letter in letters:
		# 	try:
		# 		card_dict[letter] += 1
		# 	except:
		# 		card_dict[letter] = 1

		# card_type = get_type(card_dict)
		card_type = get_new_type(letters)
		card_data.append( (card_type, int(bid), letters))

cards = sorted(card_data, key=functools.cmp_to_key(card_cmp))
# cards = list(reversed(cards))

sum = 0
for i in range(len(cards)):
	(_, bid, _) = cards[i]
	sum += bid * (i+1)

print(cards)
print(sum)