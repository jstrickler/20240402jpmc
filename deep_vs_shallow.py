from copy import deepcopy

my_list = [['a', 'b', 'c'], [1, 2, 3]]

print(my_list[0])
print(my_list[0][1])

your_list = my_list    # assign your_list to same object as my_list
print(f"{my_list = }")
print(f"{your_list = }")

my_list.append([1.5, 2.5, 3.5])
print(f"{my_list = }")
print(f"{your_list = }")

# shallow copy
her_list = list(my_list)  # list() always creates new list object OR her_list = my_list[::]
my_list.append(['red', 'black', 'green'])
print(f"{my_list = }")
print(f"{her_list = }")

my_list[0].append('d')
print(f"{my_list = }")
print(f"{her_list = }")

# deep copy
his_list = deepcopy(my_list)
my_list[0].append('e')
print(f"{my_list = }")
print(f"{his_list = }")

# alias
# a = b

# shallow copy
# a = list(b)   OR a = dict(b)  OR a = set(b)

# deep copy
# from copy import deepcopy
# a = deepcopy(b)

