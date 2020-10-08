## Exercise 1 - basic generators 🌶

### Question 1

Build a generator function that takes an integer as parameter and yields multiples of 5 up to this number. Then, call this generator with ```100``` parameter and print only the two first elements.

### Question 2

Build a generator function called ```accumulate``` such that:

```accumulate([1,2,3,4,5])``` --> 1 3 6 10 15

```accumulate([1,2,3,4,5], initial=100)``` --> 100 101 103 106 110 115

```accumulate([1,2,3,4,5], operator.mul)``` --> 1 2 6 24 120

This is similar behavior as ```itertools.accumulate```.

## Exercise 2 - generator expressions 🌶 

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

Compare these two snippets of code in terms of execution time. What method is the fastest?

### Question 2

Compare the list comprehension and the generator expression in terms of memory space. What takes 


### Question 3

Test the two functions created in *Question 1* with ```range(1000000)``` as parameter, and decorated with ```execution_time```. What method is the fastest?

Then, print the size of the list comprehension and the size of the generator expression. Which one takes the less memory?

### Question 4

In which cases is better to use a list comprehension or a generator expression?
