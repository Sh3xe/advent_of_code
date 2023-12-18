import re 

value_dict = {
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
	"9":"9",
}

pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"

file = open("input")
total = 0
for line in file.read().split("\n"):
	if line == "":
		continue

	matches = [value_dict[n] for n in re.findall( pattern,line )]
	first, last = matches[0], matches[-1]
	total += int( first + last )

print(total)