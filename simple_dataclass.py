from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str

p1 = Person("John", "Doe")
print(f"{p1.first_name = }")
print(f"{p1.last_name = }")

print(dir(Person))
print(f"{p1 = }")
print(p1)