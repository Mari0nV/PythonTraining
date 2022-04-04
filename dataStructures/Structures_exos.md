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


## Exercise 2

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




