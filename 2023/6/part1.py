

times = [40829166]
distances = [277133813491063]

# times = [71530]
# distances = [940200]

possibilities = []
for i in range(len(times)):
	Tmax = times[i]
	Drec = distances[i]
	possibility_count = 0
	for t in range(0, Tmax):
		if (Tmax - t) * t > Drec:
			possibility_count += 1

	possibilities.append(possibility_count)

print(possibilities)
prod = 1
for i in possibilities:
	prod *= i
print(prod)