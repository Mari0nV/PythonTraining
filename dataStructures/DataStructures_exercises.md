# Exercises on Python Data Structures

## Exercice 1 - Class methods & Namedtuple

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

### Question 4

Write a function taking a deck instance as parameter and returning all the cards sorted by their value.


## Exercice 2 - Sets

You are provided a dictionary containing names of candidates as keys and sets of skills as values:
```
candidates = {
    "Bob": {"Python", "C++", "SQL", "Flask"},
    "Peter": {"Python", "C#", "Javascript"},
    "Alice": {"C++", "React", "SQL"},
    "Lily": {"SQL", "Python", "Flask", "Lua"}
}
```

### Question 1

Create a class called ```ManageCandidate```, containing a dictionary attribute called ```candidates``` (which can be set in the initialization function of the class).
Write the following methods for the ```ManageCandidate``` class:
- ```add_candidate``` : add new candidate into the ```candidates``` attribute. Takes a name and a set of skills as parameters.
- ```remove_candidate``` : remove candidate from the ```candidates``` attribute given its name.
- ```add_skill``` : add a skill item into the set of skills of a candidate given its name.
- ```remove_skill``` : remove a skill item into the set of skills of a candidate given its name.
- ```get_all_skills``` : returns a set of all the skills contained in the ```candidates``` values, with no duplicates.
- ```get_common_skills``` : returns a set of the common skills between multiple candidates.
- ```lacking_skills``` : returns a set of all the skills on candidate doesn't have (compared to the set of skills computed in ```get_all_skills```.
- ```get_experts```: returns a set of the names of candidates knowing the skill passed in parameter.
- ```reverse_candidates```: returns a dictionary where each skill is a key and each value is a set of names knowing the skill. Use ```dict.setdefault``` method to fill the new dictionary.

### Question 2

Create an instance of the ```ManageCandidate``` class, taking the dictionary ```candidates``` above as parameter. Use the methods created previously to do the following steps:
- compute the list of Python developers.
- print the list of skills they all share.
- print the list of skills none of them share.
