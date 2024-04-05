import operator as op

def cleanup(s):
    return s.strip().lower()


data = ['Wombat', 'Wankel Rotary Engine',  "    anemone     ", "SUPERBAT"]

for d in data:
    print(cleanup(d))
print()

def process_strings(func, strings):
    return [func(s) for s in strings]

print(process_strings(cleanup, data))
print()
print(process_strings(str.upper, data))

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=str.lower)
print(f"{f2 = }\n")


def more_processing(strings, *funcs):
    result = strings
    for func in funcs:
        result = [func(s) for s in result]
    return result    

# lambda param ...: return-value

x = more_processing(fruits, cleanup, str.lower, lambda s: s[:3],  lambda s: ">" + s + "<")
print(f"{x = }\n")


def doit(func, value1, value2):
    return func(value1, value2)

def add_values(v1, v2):
    return v1 + v2

def substract_values(v1, v2):
    return v1 - v2

print(f"{doit(add_values, 10, 5) = }\n")
print(f"{doit(substract_values, 10, 5) = }\n")

print(f"{doit(lambda x, y: x + y, 10, 5) = }\n")
print(f"{doit(op.add, 10, 5) = }\n")
print(f"{doit(op.mul, 10, 5) = }\n")

print(f"{op.getitem(fruits, 2) = }\n")   # fruits[2]














