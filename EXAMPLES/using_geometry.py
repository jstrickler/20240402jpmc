from geometry import Number, circle_area, rectangle_area
import typing as T
import inspect


result: float

result = circle_area(50)

print(f"{result = }")
print(f"{type(result) = }")

result = circle_area(5.9)

# result = circle_area('spam')

x: int
x = rectangle_area(5, 19)
print(f"{x = }")

class Foo:
    def add_node(self, node: "Foo"):
        pass


class Bar:
    pass


def process_files(file_names: T.Iterable[str|bytes]) -> int:
    for file_name in file_names:
        print(file_name)
    return 0

my_files = ['a.txt', 'b.txt']

process_files(my_files)

my_other_files = 'c.txt', 'd.txt'
those_files = (f.upper() for f in my_files)

process_files(my_other_files)
process_files(those_files)
process_files([1,2,3])

def triple(x: T.Any) -> T.Any:
    return x * 3

print(f"{triple(5) = }")
print(f"{triple('foo') = }")

print(inspect.get_annotations(process_files))
print()

print(process_files.__annotations__)






