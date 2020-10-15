## Exercise 1 🌶🌶

The goal is to write a class ```Point``` representing a point in 2D dimension, in a nice pythonic way.

### Question 1

Write a simple class ```Point``` containing two attributes: ```x``` and ```y```. These will be initialized in the ```__init__``` method of the class.

Write the method ```move``` that can modify the values of the ```x``` and ```y``` attributes.


Write the method ```distance``` that computes the distance between two points. Formula: ![formula](https://render.githubusercontent.com/render/math?math=\sqrt{(x_2-x_1)^2%20%2B1%20(y_2%20-%20y_1)^2})

```py
p1 = Point(1, 1)
p2 = Point(2, 0)

p1.move(0, 1)  # p1.x -> 1 and p1.y -> 2
p1.distance(p2)  # returns the distance between p1 and p2
```

### Question 2

Transform the class ```Point``` into an iterable.

```py
p1 = Point(1, 2)

for coord in p1:
    print(coord)  # should output 1 then 2
```

It will simplify the implementation of other methods.

### Question 3

Implement methods such that:
```
>>> p1 = Point(1, 2)
>>> p1
Point(1, 2)
>>> print(p1)
(1, 2)
>>> p2 = Point(3, 0)
>>> p1 == p2
False
>>> p3 = Point(1, 2)
>>> p1 == p3
True
```

### Question 4

Modify the ```Point``` class to make it immutable.

```
>>> p1 = Point(1, 1)
>>> p1.x = 3
Traceback (most recent call last):
 ...
AttributeError: can't set attribute
```
