# Exercises on Sets

## Exercice 1 - Sets

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
- ```add_candidate``` : add new candidate into the ```candidates``` attribute. Takes a tuple containing a name and a set of skills as parameter.
- ```remove_candidate``` : remove candidate from the ```candidates``` attribute given its name. Takes a tuple containing a name and a set of skills as parameter.
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
