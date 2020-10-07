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
