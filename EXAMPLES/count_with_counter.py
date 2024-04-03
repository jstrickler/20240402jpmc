from collections import Counter

with open("../DATA/breakfast.txt") as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]  # create list of foods with EOL removed from line
    # foods = breakfast_in.read().splitlines()

counts = Counter(foods)  # initialize Counter object with list of foods
counts['pizza'] += 1  # add a pizza

for item, count in counts.items():  # iterate over results
    print(item, count)

print(f"{counts.most_common(5) = }")
