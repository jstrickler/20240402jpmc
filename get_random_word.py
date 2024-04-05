import random

class RandomWord:

    def __init__(self):
        with open('DATA/words.txt') as words_in:
            self._words = words_in.read().splitlines()
            random.shuffle(self._words)

    def __call__(self):
        return self._words.pop()

r = RandomWord()

for _ in range(10):
    print(f"{r() = }")
    