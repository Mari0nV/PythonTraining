# Exercises on Threads

## Exercise 1

The goal of this exercise is to implement a Wall object that can be destroyed by Rocks objects. 
The Wall object has an attribute *strength* that can take damage. It is initialized at 100.

Each Rock object is a Thread that tries to destroy the Wall, by inflicting a random damage between 1 and 10.
It takes one second for a Rock to perform this action and be available for another throw.

Launch the simulation with 5 Rocks. The output should display something like this:
```
Robot 1 did 10 damage to the wall. Remaining strength: 90
Robot 2 did 2 damage to the wall. Remaining strength: 88
Robot 4 did 4 damage to the wall. Remaining strength: 81
Robot 3 did 3 damage to the wall. Remaining strength: 85
Robot 5 did 1 damage to the wall. Remaining strength: 80
Robot 2 did 9 damage to the wall. Remaining strength: 71
Robot 1 did 8 damage to the wall. Remaining strength: 63
Robot 3 did 9 damage to the wall. Remaining strength: 44
Robot 4 did 10 damage to the wall. Remaining strength: 53
Robot 5 did 3 damage to the wall. Remaining strength: 41
Robot 2 did 9 damage to the wall. Remaining strength: 32
Robot 5 did 10 damage to the wall. Remaining strength: 22
Robot 4 did 7 damage to the wall. Remaining strength: 15
Robot 3 did 6 damage to the wall. Remaining strength: 9
Robot 1 did 7 damage to the wall. Remaining strength: 2
Robot 2 did 2 damage to the wall. Remaining strength: 0
```
