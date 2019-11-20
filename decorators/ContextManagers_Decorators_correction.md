# Correction of the exercices on decorators and context managers

## Exercice 1

### Question 1

```
class MyOpenContextManager:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.fd = open(self.file, "r")
        return fd
    def __exit__(self, type, value, traceback):
        self.fd.close()
```

### Question 2

```
from contextlib import contextmanager

@contextmanager
def my_open_func(file):
    try:
        fd = open(file, "r")
        yield fd
    finally:
        fd.close()
```

## Exercice 2

### Question 1

```
def polite(f):
    def wrapper(item):
        str = "Hello "
        str += f(item)
        str += " please"
        return str
    return wrapper
    
@polite
def i_want(item):
    return(f"I want {item}")
 ```

### Question 2

```
import sys
from io import StringIO

class PoliteContextManager:
    def __init__(self):
        self.realstdout = sys.stdout
        self.capture = StringIO()
    def __enter__(self):
        sys.stdout = self.capture
    def __exit__(self, type, value, traceback):
        sys.stdout = self.realstdout
        msg_content = self.capture.getvalue().rstrip("\n")
        print(f"Hello {msg_content} please")
```

### Question 3

Difference between decorators and context managers are that decorators are applied to a function definition whereas context managers are applied on demand.
So if you want a behavior applied each time a function is called, a decorator is the best practice.
In the case of our exercise, we want Esmeralda to be polite each time she asks for something, so using a decorator is a good idea.

### Question 4

This question can be answered very simply with ```re.sub```, however I wanted a bit of challenge and decided to use the properties of closures to do it.

```
from types import CodeType

def rewrite_func(f):
    def wrapper(item):
        return f(item)

    f_code = wrapper.__closure__[0].cell_contents.__code__
    new_co_consts = (None, "I would like ")
    wrapper.__closure__[0].cell_contents.__code__ = CodeType(
        f_code.co_argcount,
        f_code.co_kwonlyargcount,
        f_code.co_nlocals,
        f_code.co_stacksize,
        f_code.co_flags,
        f_code.co_code,
        new_co_consts,
        f_code.co_names,
        f_code.co_varnames,
        f_code.co_filename,
        f_code.co_name,
        f_code.co_firstlineno,
        f_code.co_lnotab,
        f_code.co_freevars,
        f_code.co_cellvars,
    )
    return wrapper

@polite
@rewrite_func
def i_want(item):
    return(f"I want {item}")

print(i_want("some bread")) # prints "Hello I would like some bread please"
```
