


Animal = type('Animal', (), {'move': lambda self: print("Moving...")})
a = Animal()

print(f"{Animal = }")
print(f"{a = }")
print(f"{type(a) = }")
a.move()

Dog = type('Dog', (Animal,), {'bark': lambda self: print("Woof! Woof!")})

d = Dog()
d.move()
d.bark()

