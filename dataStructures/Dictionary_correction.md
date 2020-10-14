### Exercise 1

```py
d = {keys[i]: values[i] for i in range(len(keys))}
```

or

```py
d = dict(zip(keys, values))
```

### Exercise 2

```py
d = d1.copy()
for key, value in d2.items():
    d.setdefault(key, 0)
    d[key] = value
```

or

```py
from collections import Counter

d = Counter(d1) + Counter(d2)
```
