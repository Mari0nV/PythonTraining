# Exercises on Sets

## Exercice 1 - Sets

You are provided a dictionary containing names of candidates as keys and sets of skills as values:
```
candidates = {
    "Bob": {"Python", "C++", "SQL"},
    "Peter": {"Python", "C#", "Javascript"},
    "Alice": {"C++", "React", "SQL"}
}
```

### Question

Create a class called ```ManageCandidate```, containing a dictionary attribute called ```candidates``` (which can be set in the initialization function of the class).
Write the following methods for the ```ManageCandidate``` class:
- ```add_candidate``` : add new entry into the ```candidates``` attribute.
- ```remove_candidate``` : remove candidate from the ```candidates``` attribute given its name.
- ```add_skill``` : add a skill item into the set of skills of a candidate given its name.
- ```remove_skill``` : remove a skill item into the set of skills of a candidate given its name.
- ```get_all_skills``` : returns a set f all the skills contained in the ```candidates``` values, with no duplicates.
- ```get_common_skills``` : returns a set of the common skills between two candidates.
- ```lacking_skills``` : returns a set of all the skills on candidate doesn't have (compared to the set of skills computed in ```get_all_skills```.
- ```get_experts```: returns a set of the names of candidates knowing the skill passed in parameter.
- ```reverse_candidates```: returns a dictionary where each skill is a key and each value is a set of names knowing the skill. Use ```dict.setdefault``` method to fill the new dictionary.
