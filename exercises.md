## Exercise 1 - List manipulation

### Question 1

Write a function call *word_letter_position* that takes three parameters :
- a list of string
- a letter (string)
- a position (integer)

This function must return all the words contained in the input list that contain the letter at the position specified.

You can test the following exercise with this input list :
```input_list = ['eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon',
'rickon', 'theon', 'rorbert', 'cersei', 'tywin', 'jaime',
'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor',
'varys', 'renly', 'a' ]
```

Example: ```word_letter_position(input_list, 'y', 1)``` will return ```['tywin', 'tyrion']```

### Question 2

Write a parametrized unit test with pytest (see *pytest.mark.parametrize*) that tests this function with all the corner cases possibles.

## Exercise 2 - Dictionary manipulation

You receive a dictionary that can contain dictionaries that can contains dictionaries etc... (they are called nested dictionaries).

### Question 1

Write a function that takes into parameters this dictionary and a string. The string will be under the form "key1.key2.key3...".
This function will return the value associated to the key passed in parameters if it exists, and raise an exception otherwise.

Example :
```
mydict = {
  "a": {
      "b": 33
    }
}
get_value(mydict, "a.b")  # will return 33
```

### Question 2

Write a parametrized unit test with pytest (see *pytest.mark.parametrize*) that tests this function with all the corner cases possibles.
Also write a unit test testing if the function correctly raises an exception if the key requested is not found in the dictionary.

## Exercice 3 - Class methods & Namedtuple

### Question 1

Create a ```namedtuple``` object called ```Card``` containing two attributes: ```rank``` and ```suits```. Then create a list of 52 ```Card``` objects, one for each rank and suit that can be found in some french decks : *2,3...10, J, Q, K, A* for the ranks; and *spades, diamonds, hearts and clubs* for the suits.

### Question 2

Create a class ```Deck``` containing the list created previously as an attribute (set in the initialization method).
Write custom methods for this class such that the following assertions return ```True```:
```
deck = Deck()

assert len(deck) == 52
assert isinstance(deck[0], Card)
```

### Question 3

Write a method ```card_value``` which returns the value of the card passed in parameter, considering that *spades > diamonds > hearts > clubs*. For example, the 2 of spades will have a greater value than the 2 of diamonds, which will have a greater value than the 2 of hearts etc...
- 2 of clubs: 0
- 2 of hearts: 1
- 2 of diamonds: 2
- 2 of spades: 3
- 3 of clubs: 4

     ⋮
- As of spades: 51

## Exercise 4 - base64 and string manipulation

You receive a string encoded in base64. You know that once decoded, this string has the following format :

```
machine<id>?:<name>@<vendor>?:<password>@<year>
```

where *id* and *year* are integers, *name* and *vendor* are alphanumerical strings, and *password* is a string that can contain alphanumerical values, integers or the following special characters: ```.?@!:```.

### Question 1

Write a function that can decode the encoded string and return the password.

You can test your function with the following inputs :

```
bWFjaGluZTE/OmJvYkBtYW1hem9uPzpzaW1wbGVwYXNzd29yZDFAMjAzMg==    # should output simplepassword1
bWFjaGluZTI/OmFsaWNlQGFsaWJvdWJvdT86cFJmP2dsMTJATUAyMDMy    # should output pRf?gl12@M
bWFjaGluZTM/Om1hcnRpbkBzbmFjPzptZHA/OmJiOEAyMDMz    # should output mdp?:bb8
bWFjaGluZTQ/OmVsb0BkYXJweT86QGM/NEBAZ3JyPzpAMjAzMw==    # should output @c?4@@grr?:
```

### Question 2

Write a parametrized unit test with pytest (see *pytest.mark.parametrized*) testing the previous function with the given inputs.

## Exercise 5 - decorators

### Question 1

Write a *multiply* function that multiply two numbers and return the result.

Write a decorator that cache the parameters and result of each call to *multiply* into a global dictionary.

Before each call to **multiply**, verify if it was already called before with the same parameters by looking at the dictionary. If it was already, just return the result stored in the dictionary and don't call **multiply**.

Look of the global dictionary:
```
cache = {
 (1, 2): 2,
 (3, 5): 5,
 ...
}
```

### Question 2

Write a decorator that limit the number of executions authorized for a function. This decorator will take a parameter **nb_executions** that represent the max of executions authorized. If a decorated function was called too many times, raise a customized exception called **LimitExcedeed**.


## Exercise 6 - Flask decorator

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


