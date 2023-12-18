import re
import time
import timeit

SEED_TO_SOIL = "seed-to-soil map:"
SOIL_TO_FERT = "soil-to-fertilizer map:"
FERT_TO_WATR = "fertilizer-to-water map:"
WATR_TO_LIGT = "water-to-light map:"
LIGT_TO_TEMP = "light-to-temperature map:"
TEMP_TO_HUMD = "temperature-to-humidity map:"
HUMD_TO_LOCA = "humidity-to-location map:"

mapping = {}
seeds = []

def get_correspondance(mapping_key, key):
	global mapping
	lst = mapping[mapping_key]
	for (value_begin, key_begin, range_len) in lst:
		if key_begin <= key < key_begin + range_len:
			return value_begin + (key - key_begin)
	return key

def get_location(seed):
	global mapping
	soil = get_correspondance(SEED_TO_SOIL, seed)
	fert = get_correspondance(SOIL_TO_FERT, soil)
	watr = get_correspondance(FERT_TO_WATR, fert)
	ligt = get_correspondance(WATR_TO_LIGT, watr)
	temp = get_correspondance(LIGT_TO_TEMP, ligt)
	humd = get_correspondance(TEMP_TO_HUMD, temp)
	loca = get_correspondance(HUMD_TO_LOCA, humd)
	return loca

def parse_input(path):
	global mapping, seeds
	with open(path) as file:
		lines = file.read().split("\n")
		seeds = [(int(seed)) for seed in re.findall("[0-9]+", lines[0])]
		
		i = 1
		while i < len(lines):

			if lines[i] == "":
				i += 1
				continue

			key = lines[i]
			mapping[key] = []
			i += 1
			while i < len(lines) and lines[i] != "":
				(value_begin, key_begin, range_len) = re.findall("([0-9]+) ([0-9]+) ([0-9]+)", lines[i])[0]
				mapping[key].append( (int(value_begin), int(key_begin), int(range_len)) )
				i += 1


parse_input("input2")

minimum = 999999999999999
for i in range(0, len(seeds), 2):
	seed_beg = seeds[i]
	seed_len = seeds[i+1]
	for seed in range(seed_beg, seed_beg+seed_len):
		minimum = min(get_location(seed), minimum)
	print(minimum)
print( minimum )