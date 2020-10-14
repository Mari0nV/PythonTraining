## Exercise 1 🌶

### Question 1

Write a decorator ```time_exec``` that computes and print the execution time of a function.

You can test it on the function below:

```py
@time_exec
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result += i
    return result
```

### Question 2

Modify the previous decorator such that it also prints the name, the arguments and the result of the decorated function.

For example, decorating the previous ```factorial``` function will output:

```
factorial(6) -> 720 in 0.00001097s
```


### Question 3

Modify the previous decorator such that it can take a ```digits``` parameter, corresponding to the number of digits you want to see printed.

```py
@time_exec(5)  # Will print execution time with 5 digits after comma
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result += i
    return result
```






