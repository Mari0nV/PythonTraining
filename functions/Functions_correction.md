## Exercise 1 - Dunder methods, inspect and print

### Question 1
```
def doc_function(*functions):
    columns = ["name", "arg_names", "description"]
    dash = '-' * 100

    print(dash)
    print('{:<15s}{:<15s}{:<40s}'.format(*columns))
    print(dash)
    for func in functions:
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        row = [
            func.__name__,
            ', '.join(arg_names),
            func.__doc__,
            ]
        print('{:<15s}{:<15s}{:<40s}'.format(*row))
    
    print(dash)
```

Explanation of the ```{:<15s}``` in ```format```: it means that 15 spaces will be allocated to print the string (*s* symbol), which will be aligned left (*<* symbol). We could also have use the tabulate module (package python-tabulate) which create very pretty tables.

### Question 2
```
def doc_function_inspect(*functions):
    columns = ["name", "arg_names", "description"]
    dash = '-' * 100

    print(dash)
    print('{:<15s}{:<15s}{:<40s}'.format(*columns))
    print(dash)
    for func in functions:
        sig = signature(func)
        row = [
            func.__name__,
            ', '.join(sig.parameters.keys()),
            getdoc(func),
            ]
        print('{:<15s}{:<15s}{:<40s}'.format(*row))
    
    print(dash)
```

The use of ```inspect``` module is recommended instead of using only dunder methods of the function object. Indeed in *Question 1* the function ```doc_function``` does not work for built-in functions.

## Exercise 2

```
def dont_mind_me(func):
    code = func.__code__

    # Creating new co_code for func
    new_co_code = []
    for opcode in code.co_code:
        # Replacing multiply operator by add operator
        if dis.opname[opcode] == 'BINARY_MULTIPLY':
            new_co_code.append(dis.opmap['BINARY_ADD'])
        else:
            new_co_code.append(opcode)
    
    # Creating new co_consts
    new_co_consts = []
    for const in code.co_consts:
        # Replacing 10 constant by 1
        if const == 10:
            new_co_consts.append(1)
        else:
            new_co_consts.append(const)
    
    # Replacing func.__code__ with new code object
    func.__code__ = type(code)(
        code.co_argcount,
        code.co_kwonlyargcount,
        code.co_nlocals,
        code.co_stacksize,
        code.co_flags,
        bytes(new_co_code), # modified co_code
        tuple(new_co_consts), # modified co_consts
        code.co_names,
        code.co_varnames,
        code.co_filename,
        code.co_name,
        code.co_firstlineno,
        code.co_lnotab,
        code.co_freevars,
        code.co_cellvars
    )
```
