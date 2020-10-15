## Exercise 1

### Question 1

```py
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self, point):
        dx = point.x - self.x
        dy = point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
```

### Question 2

We implement the dunder method ```__iter__``` inside the ```Point``` class.

```py
def __iter__(self):
        return (i for i in (self.x, self.y))
```

### Question 3

We implement the following dunder methods:

```py
    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.x}, {self.y})"
 
    def __eq__(self, point):
        return tuple(self) == tuple(point)
```

### Question 4

```py
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    def move(self, x, y):
        self.__x += x
        self.__y += y
 ```
 
 The other dunder methods can stay the same. 
 
 The ```__x``` and ```__y``` are not completely private since they can be modified this way:
 ```
 >>> p1 = Point(1, 2)
 >>> p1._Point__x = 3
 >>> p1._Point__y = 3
 >>> p1
 Point(3, 3)
 ```
 
This feature is called *name mangling*.

Protecting attributes in Python is just a way to prevent accidental overwriting of "private" attributes, but it is not a security measure.
