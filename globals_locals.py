
a = "apple"

def spam():
    print("SPAM SPAM SPAM")

g = globals()
print(f"{g = }\n")

print(f"{g['a'] = }")
g['spam']()

g['color'] = 'blue'

print(f"{color = }")

g['scream'] = lambda : print("AAAAAHHHHHHHHHH")

scream()


def ham():
    x = 10
    name = "Bob"
    print(f"{locals() = }")

ham()

