## Exercise 1 - basic generators 🌶

### Question 1

Build a generator function called ```multiples``` that takes an integer as parameter and yields multiples of 5 up to this number.

```multiples(16)``` --> 5 10 15

Then, call this generator with ```20``` parameter and print only the first element.

### Question 2

Build a generator function called ```accumulate``` such that:

```accumulate([1,2,3,4,5])``` --> 1 3 6 10 15

```accumulate([1,2,3,4,5], initial=100)``` --> 100 101 103 106 110 115

```accumulate([1,2,3,4,5], operator.mul)``` --> 1 2 6 24 120

This is similar behavior as ```itertools.accumulate```.

### Question 3

Build a generator function called ```cycle``` such that:

```cycle('ABCD')``` --> A B C D A B C D A B C D ...

This is similar behavior as ```itertools.cycle```.

## Exercice 2 - class generators 🌶🌶

Implement two classes called ```AccumulateGenerator``` and ```CycleGenerator``` which have the same behavior as the functions ```accumulate``` and ```cycle``` from *Exercise 1*.

```py 
accumulate = AccumulateGenerator([1,2,3,4,5])
for value in accumulate:
    print(value)  # 1 3 6 10 15

cycle = CycleGenerator('ABCD')
for value in cycle:
    print(value)  # A B C D A B C D A B C D ...
```


## Exercise 3 - generator expressions 🌶 

In this exercise, we consider these two snippets of code:
```py
s = 0
for elt in [i for i in range(1000000)]:
    s += elt
```

```py
s = 0
for elt in (i for i in range(1000000)):
    s += elt
```

### Question 1

Compare these two snippets of code in terms of execution time. Which method is the fastest?

### Question 2

Compare the list comprehension and the generator expression in terms of memory space. Which one takes the least memory?

### Question 4

In which cases is it better to use a list comprehension or a generator expression?

