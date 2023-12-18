import re

values = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
	"1":"1",
	"2":"2",
	"3":"3",
	"4":"4",
	"5":"5",
	"6":"6",
	"7":"7",
	"8":"8",
	"9":"9"
}

def parse_line( line ):
	numbers = re.findall("one|two|three|four|five|six|seven|eight|nine|[1-9]", line)
	return [values[n] for n in numbers]

file = open("input", "r")

lines = file.read().split("\n")
total = 0
print(parse_line("zoneight234"))

# lines = ["two1nine", "eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]

# for line in lines:
# 	if( len(line) <= 0 ):
# 		continue
	
# 	parsing = parse_line(line)
# 	first, last = parsing[0], parsing[-1]
# 	total += int(first + last)

# print(total)