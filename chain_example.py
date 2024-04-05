from itertools import chain

names1 = ['Fred', 'Bob', 'Maria', 'Abdul', 'Prytha']

names2 = "Roberto", 'Ivan', 'Srini', 'Paul'

names3 = ['Ali', 'Brenda', 'Bethany']

stuff = "abcde"

for name in chain(names1, names2, names3, stuff):
    print(name, end=" ")
print()

