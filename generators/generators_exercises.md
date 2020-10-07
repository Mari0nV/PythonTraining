## Exercise 1 🌶

### Question 1

Build a generator function that takes an integer as parameter and yields multiples of 5 up to this number. Then, call this generator with ```100``` parameter and print only the two first elements.

### Question 2

Build a generator function called ```accumulate``` such that:

```accumulate([1,2,3,4,5])``` --> 1 3 6 10 15

```accumulate([1,2,3,4,5], initial=100)``` --> 100 101 103 106 110 115

```accumulate([1,2,3,4,5], operator.mul)``` --> 1 2 6 24 120

This is similar behavior as ```itertools.accumulate```.
