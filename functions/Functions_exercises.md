## Exercise 1 - Dunder methods, inspect and print - **

In this exercise, you will implement a function called ```doc_function``` which take one or more user-defined function as parameters. 
The role of this function is to print the name, the parameter names and the docstring of each parameter.

To test your function, you can use these two user-defined functions as parameters:
```
def hypot(a, b):
    """Returns the hypotenuse of a right-angled triangle"""
    c = a ** 2 + b ** 2
    return sqrt(c)

def factorial(n):
    """Returns the factorial of the number n"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

The output of ```doc_function(hypot, factorial)``` will look like this:
```
----------------------------------------------------------------------------------------------------
name           arg_names      description                             
----------------------------------------------------------------------------------------------------
hypot          a, b           Returns the hypotenuse of a right-angled triangle
factorial      n              Returns the factorial of the number n                       
----------------------------------------------------------------------------------------------------
```

### Question 1

Implement the ```doc_function``` using only dunder methods of the function object.

### Question 2

Implement the ```doc_function``` using the ```inspect``` module. You'll be able to use your ```doc_function``` on built-in functions as well.
For example, you can pass the ```operator.add``` function as a parameter. The final output will be:
```
----------------------------------------------------------------------------------------------------
name           arg_names      description                             
----------------------------------------------------------------------------------------------------
hypot          a, b           Returns the hypotenuse of a right-angled triangle
factorial      n              Returns the factorial of the number n   
add            a, b           Same as a + b.                          
----------------------------------------------------------------------------------------------------
```

## Exercise 2 - Dunder methods, dis module - ***

The goal of this exercise is to modify the function below at runtime.
```
def multiply_by_10(n):
    return n * 10
```

Implement a function called ```dont_mind_me``` which take the function above as a parameter 
and change the *10* constant by *1* and the *multiply* operator by an *add* operator.

You can test it with the code below:
```
def compute_things():
    print("First call to multiply_by_10:")
    for i in range(5):
        result = multiply_by_10(i)
        print(f"{i} * 10 = {result}")

    dont_mind_me(multiply_by_10)

    print("Second call to multiply_by_10:")
    for i in range(5):
        result = multiply_by_10(i)
        print(f"{i} * 10 = {result}")
```

The ouput of ```compute_things()``` will be:
```
First call to multiply_by_10:
0 * 10 = 0
1 * 10 = 10
2 * 10 = 20
3 * 10 = 30
4 * 10 = 40
Second call to multiply_by_10:
0 * 10 = 1
1 * 10 = 2
2 * 10 = 3
3 * 10 = 4
4 * 10 = 5
```

