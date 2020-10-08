## Exercise 1

### Question 1

```py
def multiples(limit):
    for nb in range(1, limit):
        if nb % 2 == 0 or nb % 5 == 0:
            yield nb

multiples_gen = multiples(10)
print(next(multiples_gen), next(multiples_gen))
```

### Question 2

```py
import operator

def accumulate(iterable, op=operator.add, initial=None):
    
    iterable = iter(iterable)
    total = initial if initial else next(iterable)
    
    for i in iterable:
        total = op(total, i)
        yield total
```

## Exercise 2

### Question 1

```py
import time

start = time.time()
s = 0
for elt in [i for i in range(1000000)]:
    s += elt
end = time.time()
print("duration list comprehension:", end - start)

start = time.time()
s = 0
for elt in (i for i in range(1000000)):
    s += elt
end = time.time()
print("duration generator expression:", end - start)
```

It gives the output:
```
uration list comprehension: 0.2386188507080078
duration generator expression: 0.2069690227508545
```

Using a generator expression is slightly faster.

### Question 2

```py
from sys import getsizeof

print("size of list comprehension:", getsizeof([i for i in range(10000000)]))
print("size of generator expression:", getsizeof((i for i in range(10000000))))
```

It gives the output:

```
size of list comprehension: 81528064
size of generator expression: 128
```

Generator expressions are clearly more memory-efficient.

### Question 3

Generator expressions are great to use when elements need to be iterated only once and don't need to be modified.

## Exercise 3

```py
import random


def do_action(urns):  # generator used to perform random choices
    while True:
        choices = ["heads", "tails"]
        choice = random.choice(choices)

        yield choice
        yield random.choice(urns[choice])


def play_game(urns, scores):  # function calling the generator and containing the game loop
    score = 0
    play = do_action(urns)

    print("Press Enter to toss a coin or pick a ball.")
    turns = 0
    while score > -40 and score < 40:
        turns += 1
        input("Toss a coin:")
        choice = next(play)
        input(f"You got {choice}.\nPick a ball:")
        color = next(play)
        score += scores[color]
        print(f"You got a {color} ball.\nScore: {score}\n")

    if score <= -40:
        print(f"You lost in {turns} turns!")
    else:
        print(f"You won in {turns} turns!")

if __name__ == '__main__':
    urns = {
    "heads": ["black", "black", "white"],
    "tails": ["black", "black", "white", "white", "red"],
    }

    scores = {"black": -3, "white": 1, "red": 20}

    play_game(urns, scores)
```
