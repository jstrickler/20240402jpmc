

x = [1, 2, 3]

print(f"{hasattr(x, '__iter__') = }")
print(f"{hasattr(x, '__next__') = }")

# print(f"{next(x) = }")
x_iter = iter(x)
print(f"{hasattr(x_iter, '__iter__') = }")
print(f"{hasattr(x_iter, '__next__') = }")
print(f"{next(x_iter) = }")
print(f"{next(x_iter) = }")
print(f"{next(x_iter) = }")
# print(f"{next(x_iter) = }")

f = open('DATA/mary.txt')
print(f"{f = }")
print(f"{hasattr(f, '__iter__') = }")
print(f"{hasattr(f, '__next__') = }")
first_line = next(f)
print(f"{first_line = }")
for raw_line in f:
    line = raw_line.rstrip()
    print(line)

