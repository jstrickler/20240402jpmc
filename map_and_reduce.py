#  map and reduce
from functools import reduce

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

ucfruits = map(str.upper, fruits)
print(f"{ucfruits = }\n")
for fruit in ucfruits:
    print(fruit)
print('-' * 60)

ucfruits_gen = (f.upper() for f in fruits)  #  generator expression


