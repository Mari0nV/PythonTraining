# Exercises on Python Data Structures

## Exercice 1 - List manipulation

For the following exercise, there is a pythonic way of doing each question. So don't just do *for* loops when it's not necessary!

Write small snippets of codes that take a list of integers as input and do the following actions:

### Question 1

Remove duplicates from the list.

Example:
```[1, 2, 3, 1, 5]``` becomes ```[1, 2, 3, 5]```

### Question 2

Print the last element of the list.

### Question 3

Create a new list that contains each element of the previous list multiplied by 4.

### Question 4

Compute the sum of each odd number of the list.

### Question 5

Print the three first elements of the list.

### Question 6

Print the list in reverse order.

### Question 7

Find two ways to order the list: one that modify the list, the other that does not modify it.

## Exercice 2 - Dict manipulation

### Question 1

Create a dictionary from the following list:
```[("A",1),("B",2),("C",3)]```

### Question 2

From the previous dictionary, print the list of keys with the following format:
```
A
B
C
```

### Question 3

Add two new items in the previous dictionary : *(C, 4)* and *(D, 5)*

### Question 4

Multiply all the values of the dictionary by 2.

### Question 5

Delete the item (A, 2) from the dictionary.

### Question 6

Print the sum of all values contained in the dictionary.


## Exercise 3 - List manipulation

You can test the following exercise with this input list :
```input_list = ['eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon',
'rickon', 'theon', 'rorbert', 'cersei', 'tywin', 'jaime',
'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor',
'varys', 'renly', 'a' ]
```

Write a function call word_letter_position that takes three parameters :
- a list of string
- a letter (string)
- a position (integer)

This function must return all the words contained in the input list that contain the letter at the position specified.

example: ```word_letter_position(input_list, 'y', 1)``` will return ```['tywin', 'tyrion']```

## Exercise 4 - Strings

### Question 1

Write a function that decompose a database url and create a dictionary containing the fields user, password, host, db_name and port.

Example:

Input : ```"postgresql://some_user:password123@my_db_uri/my_db_name:5432"``` 

Expected_output: 
```
{
  "user": "some_user",
  "password": "password",
  "host": "my_db_uri",
  "db_name": "my_db_name",
  "port": 5432 
}
```

### Question 2

Write a function that detects if a string is a palindrome or not.

### Question 3

Write a function that takes a paragraph as input and return a list of sentences.
Each sentence letter must being with an Uppercase letter and end with a punctuation letter.

Example

Input:
```
"in Python, there is three distinct numeric types. integers, floating points and complex numbers! in addition, Booleans are a subtype of Integers"
```

Expected output:
```
["In Python, there is three distinct numeric types.", "Integers, floating points and complex numbers!", "In addition, Booleans are a subtype of Integers."]
```

### Question 4

Given the list of sentences obtained in previous question, create a dictionary which associate each word found with its number of occurrence in the list. It will be case insensitive.

Example

Input:
```
["In Python, there is three distinct numeric types.", "Integers, floating points and complex numbers!", "In addition, Booleans are a subtype of Integers."]
```

Expected output:
```
{
  "in": 2,
  "python": 1,
  "there": 1,
  "is": 1,
  ...
}
```




