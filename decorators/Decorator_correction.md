## Exercise 1

### Question 1

```py
import time


def time_exec(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print("Duration: {:.8f}".format(end - start))
        return result

    return timed
```

### Question 2

```py
def time_exec(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        pretty_args = ", ".join(args)
        if kwargs:
            pretty_kwargs = ", ".join(f"{key}={value}" for key, value in kwargs.items())
            pretty_args += f", {pretty_kwargs}"

        print(
            "{}({}) --> {} ({:.8f}s)".format(
                func.__name__, pretty_args, result, end - start
            )
        )
        return result

    return timed
```

### Question 3

```py
def time_exec(unit=None):
    def decorator(func):
        def timed(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            pretty_args = ", ".join(args)
            if kwargs:
                pretty_kwargs = ", ".join(
                    f"{key}={value}" for key, value in kwargs.items()
                )
                pretty_args += f", {pretty_kwargs}"

            if unit == "ms":
                elapsed = "{:.8f}ms".format((end - start) * 1000)
            else:
                elapsed = "{:.8f}s".format(end - start)

            print(
                "{}({}) --> {} ({})".format(func.__name__, pretty_args, result, elapsed)
            )
            return result

        return timed

    return decorator
 ```
 
 ## Exercise 2
 
 ```py
 class App:
    def __init__(self):
        self.route_dict = {}

    def route(self, url, methods=None):
        def wrapped(func):
            for method in methods:
                self.route_dict.setdefault(method, []).append({url: func.__name__})

        return wrapped
 ```
