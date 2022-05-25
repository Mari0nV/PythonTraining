# Chiffrement Vigenere modifié

Ecrivez une fonction qui prend en entrée un message et une clé de chiffrement, qui le chiffre en suivant un algorithme Vigenere modifié et retourne le message chiffré.

## Rappel Algorithme Vigenere

Le chiffrement de chaque lettre du message correspond à son rang dans l'alphabet + le rang d'une lettre de la clé de chiffrement modulo 26.

Par exemple avec le message *CODE* à chiffrer et la clé *AIR* :

Lettre C : rang 2 (on part de 0) + rang 0 (lettre A) -> 2 -> C

Lettre O : rang 14 + rang 8 (lettre I) -> 22 -> W

Lettre D : rang 3 + rang 17 (lettre R) -> 20 -> U

Lettre E : rang 4 + rang 0 (lettre A) -> 4 -> E

Le mode chiffré ici sera *CWUE*.

## Algorithme Vigenere modifié

Dans cet exercice, on considère un algorithme de Vigenere légèrement différent.

Pour chaque lettre de clé, au lieu d'avoir la correspondance *A=0,B=1,...,Z=25*, on aura la correspondance suivante :
```
A=1
B=0
C=3
D=2
E=5
F=4
G=7
...
Y=25
Z=24
```

Ce qui donnera pour notre exemple :

Lettre C : rang 2 (on part de 0) + rang 1 (lettre A) -> 3 -> D

Lettre O : rang 14 + rang 9 (lettre I) -> 23 -> X

Lettre D : rang 3 + rang 16 (lettre R) -> 19 -> T

Lettre E : rang 4 + rang 1 (lettre A) -> 5 -> F

Le mode chiffré ici sera *DXTF*.

Tout caractère qui n'est pas une lettre de l'alphabet sera supprimé.

## Exemple


### Paramètres d'entrée
```
vigenere_modifie(message, key)
```

### Sortie attendue

```
dxtf
```
