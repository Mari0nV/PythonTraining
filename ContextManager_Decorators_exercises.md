# Exercises on decorators and context managers

## Exercice 1 - Context managers

A context manager provides a way to automatically execute some instructions before and after a block of code. 
It can be defined as a class containing the ```__enter__``` and ```__exit__``` methods.

You probably know the following python syntax:
```
with open("file.txt", "r") as fd:
    print(fd.read())
```

In the following questions, you will be asked to re-implement this context manager using two different methods. 

### Question 1

Write your own context manager such that the following code is doing the same as the previous one:

```
with MyOpenContextManager("file.txt") as fd:
    print(fd.read())
```

### Question 2

Same question but using the module contextlib.contextmanager

```
with my_open_func("file.txt") as fd:
    print(fd.read())
```

## Exercice 2 - Decorators and context managers

Young Esmeralda is not very polite yet. When she goes to the bakery, she just ask for what she wants in an abrupt way.

```
def i_want(item):
  return(f"I want {item}")
```

Her mother is not pleased with that and wants her to learn to say "Hello" beforehand and "Please" afterwards.

### Question 1

Write a decorator that add *Hello* before Esmeralda's message and *please* afterwards.

```
@polite
def i_want(item):
  return(f"I want {item}")

print(i_want("some bread")) # must print "Hello I want some bread please" 
```

### Question 2

Write a context manager that does the same thing.

```
with PoliteContextManager():
    print(i_want("some bread")) 
# must print "Hello I want some bread please"
```

### Question 3

In which case is it better to implement a decorator instead of a context manager?

### Question 4 (bonus)

Esmeralda's mother is still not happy, and wants Esmeralda to say "I would like" instead of "I want".
Find a way to make it happen without modifying the *i_want* function, with the help of a decorator.

```
@polite
@rewrite_func
def i_want(item):
    return(f"I want {item}")

print(i_want("some bread")) # must print "Hello I would like some bread please"
```
