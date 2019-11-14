# Exercises on Threads

## Exercise 1

The goal of this exercise is to implement a Wall object that can be destroyed by Rocks objects. 
The Wall object has an attribute *strength* that can take damage. It is initialized at 100.

Each Rock object is a Thread that tries to destroy the Wall, by inflicting a random damage between 1 and 10.
It takes one second for a Rock to perform this action and be available for another throw.

Launch the simulation with 5 Rocks. The output should display something like this:
```
Robot 2 did 9 damage to the wall. Remaining strength: 91
Robot 1 did 10 damage to the wall. Remaining strength: 81
Robot 0 did 10 damage to the wall. Remaining strength: 66
Robot 3 did 3 damage to the wall. Remaining strength: 63
Robot 4 did 5 damage to the wall. Remaining strength: 76
Robot 1 did 4 damage to the wall. Remaining strength: 59
Robot 4 did 6 damage to the wall. Remaining strength: 53
Robot 0 did 8 damage to the wall. Remaining strength: 43
Robot 2 did 2 damage to the wall. Remaining strength: 51
Robot 3 did 4 damage to the wall. Remaining strength: 39
Robot 4 did 10 damage to the wall. Remaining strength: 29
Robot 2 did 8 damage to the wall. Remaining strength: 21
Robot 0 did 6 damage to the wall. Remaining strength: 8
Robot 3 did 6 damage to the wall. Remaining strength: 15
Robot 1 did 1 damage to the wall. Remaining strength: 14
Robot 0 did 7 damage to the wall. Remaining strength: 1
Robot 1 did 2 damage to the wall. Remaining strength: 0
```
