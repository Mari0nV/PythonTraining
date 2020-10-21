## Exercise 1

### Question 1

```py
def multiples(limit):
    for nb in range(1, limit):
        if nb % 2 == 0 or nb % 5 == 0:
            yield nb

multiples_gen = multiples(20)
print(next(multiples_gen))
```

### Question 2

```py
def cycle(s):
    elts = list(s)

    while elts:
        for elt in elts:
            yield elt


c = cycle("ABCD")
for i in range(20):
    print(next(c))
```

### Question 3

```py
import operator


def accumulate(iterable, op=operator.add, initial=None):
    
    iterable = iter(iterable)
    total = initial if initial else next(iterable)
    yield total
    
    for i in iterable:
        total = op(total, i)
        yield total
```

## Exercise 2

### Question 1

```py
class CycleGenerator:
    def __init__(self, s):
        self.elts = list(s)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        elt = self.elts[self.index]
        self.index = (self.index + 1) % len(self.elts)
        return elt
```

### Question 2

```py
import operator


class AccumulateGenerator:
    def __init__(self, iterable, op=operator.add, initial=None):
        self.iterable = iter(iterable)
        self.op = op
        self.next = initial if initial else next(self.iterable)
        self.total = self.next
        self.last = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.next:
            total = self.total
            try:
                self.next = next(self.iterable)
                self.total = self.op(self.total, self.next)
            except StopIteration:
                self.next = None
            return total
        else:
            raise StopIteration()
```

## Exercise 3

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
