

#   Java:this::Python:self

class Person:
    def __init__(self, first_name, last_name):
        "Person constructor"
        self._first_name = first_name
        self._last_name = last_name
    
    # def get_first_name(self):  # getter method
    #     return self._first_name

    @property
    def first_name(self):  # getter property
        return self._first_name

    @first_name.setter
    def first_name(self, name):  # setter property
        if isinstance(name, str):
            self._first_name = name
        else:
            raise TypeError("Name must be a str")
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def last_name_upper(self):
        return self._last_name.upper()

    def __eq__(self, other):
        return (self.first_name == other.first_name) and (self.last_name == other.last_name)
    
    def __hash__(self):
        return hash(self.first_name + self.last_name)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # # dunder method
    # def __function__(self, ...):
    #     pass

p1 = Person("Wally", "Smith")  # Person p1 = new Person("Wally", "Smith");
p2 = Person("Mary", "McCoy")

print(p1.first_name, p1.last_name)

# print(p1.get_first_name())

# fn = Person.get_first_name(p1)

print(p1 == p2)
p3 = Person("Wally", "Smith")

print(f"{p1 is p3 = }")
print(f"{p1 == p3 = }")

s = set()
s.add(p1)
s.add(p2)
s.add(p3)
s.add(p1)
s.add(p1)
s.add(p3)
print(f"{s = }")
print(len(s))
print(s)
for item in s:
    print("Item:", item)


with open('DATA/mary.txt') as mary_in:
    pass

class MyContextManager:
    def __enter__(self):
        print("Entering...")
        return 42

    def __exit__(self, exc_type, exc_value, tb):
        print("Exiting")

with MyContextManager() as foo:
    print("Top of manager block")
    print(f"{foo = }")
print("All done")

