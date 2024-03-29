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

Modify the previous decorator such that it can take an optional ```unit``` parameter. If ```unit``` is equal to "ms", then the execution time must be printed in milliseconds. Otherwise, it will be printed in seconds.

```py
@time_exec("ms")  # Will print execution time in ms
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result += i
    return result
```

## Exercise 2 🌶

### Question 1

Write a **multiply* function that multiply two numbers and return the result.

Write a decorator that cache the parameters and result of each call to *multiply* into a global dictionnary.

Before each call to **multiply**, verify if it was already called before with the same parameters by looking at the dictionary. If it was alreayd, just return the result stored into the dictionary instead of calling **multiply**.

### Question 2

Write a decorator that limit the number of executions authorized for a function. This decorator will take a parameter **nb_executions** that represent the max of executions authorized. If a decorated function was called too many times, raise a customized exception called **LimitExcedeed**.

## Exercise 3 🌶🌶

In this exercise, we're going to 'mimick' Flask decorators in a very simplified way.

Create a class ```App``` such that the following code registers the decorated functions into
a ```route_dict``` dictionary.

For example, for this code:
```py
app = App()

@app.route("/", methods=["GET", "POST"])
def index():
    return "Welcome"

@app.route("/new_user", methods=["POST"])
def user():
    print("Added user")

print(app.route_dict)
```

```app.route_dict``` will look like:

```py
{
   'GET': [{'/': 'index'}],
   'POST': [{'/': 'index'}, {'/new_user': 'user'}]
}
```





