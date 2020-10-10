## Exercise 1 - basic generators 🌶

### Question 1

Build a generator function that takes an integer as parameter and yields multiples of 5 up to this number.

```multiples(16)``` --> 5 10 15

Then, call this generator with ```100``` parameter and print only the first element.

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

Compare these two snippets of code in terms of execution time. Which method is the fastest?

### Question 2

Compare the list comprehension and the generator expression in terms of memory space. Which one takes the least memory?

### Question 4

In which cases is it better to use a list comprehension or a generator expression?

## Exercise 2 - generators 🌶🌶 

In this exercise, we will implement a luck game using a generator to yield each result.

The player first toss a coin, which result in heads or tails. If he gets heads, then he picks a ball from an urn containing white, black or red balls, and if he gets tails, he picks a ball from another urn.

If the player gets a black ball, he looses 3 points. If he gets a white ball, he wins 1 point, and if he gets a red ball, he wins 20 points.

The game ends when his score reaches -40 or 40.

The urns contains the following:
```py
urns = {
    "heads": ["black", "black", "white"],
    "tails": ["black", "black", "white", "white", "red"],
}
```

The player only has to press Enter on his console to either toss a coin or pick a ball.

The output will look like:

```
Press Enter to toss a coin or pick a ball.
Toss a coin:
You got tails.
Pick a ball:
You got a red ball.
Score: 20

Toss a coin:
You got heads.
Pick a ball:
You got a black ball.
Score: 17
```


