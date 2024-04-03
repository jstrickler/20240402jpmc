

class Wombat:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return [self.name, other.name]
    
    def __str__(self):
        return f"A wombat named {self.name}"


wombat1 = Wombat("Wanda")
wombat2 = Wombat("Wally")

result = wombat1 + wombat2
print(f"{result = }")

print(wombat1)
print(wombat2)
