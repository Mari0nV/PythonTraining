# Ex 1

## Question 1

Ecrire une fonction qui prend en paramètres une chaîne de caractères encodée en base 64. Une fois décodée, vous vous apercevez qu'il s'agit d'une URL de base de données ayant le format suivant :
postgresql://<user>:<password>@<host_name>/<db_name>
Votre fonction doit décoder cette chaîne de caractères et retourner un dictionnaires du type :
```
{
    user: <user>,
    password: <password>,
    host: <host_name>,
    db: <db_name>
}
```

Le mot de passe peut contenir l'un de ces caractères spéciaux :
```! . / @ $ _```

### Tests pour le mot de passe

Paramètre d’entrée : ```cG9zdGdyZXNxbDovL2JvYjpwd2QxMjNAZGIuY2x1c3Rlci5sb2NhbC9ib2JfZGI=```

Le mot de passe sera ```pwd123```
  
  
Paramètre d’entrée : ```cG9zdGdyZXNxbDovL3Bvc3RncmVzOnB3ZEAxMjM/QGxvY2FsaG9zdC91c2Vycw==```

Le mot de passe sera ```pwd@123?```
  
  
Paramètre d'entrée : ```cG9zdGdyZXNxbDovL3RpX3RpOmEuLy9teXB3ZF8kYUBAbXkuZGIudXJsL3RhdGE=```
 
Le mot de passe sera ```a.//mypwd_$a@```

  
## Question 2
  
Transformer cette fonction en classe contenant plusieurs méthodes. Certaine(s) méthode(s) pourront être placées à l'extérieur de la classe.
  
## Question 3
  
Effectuer des tests unitaires avec Pytest et vérifier le coverage avec pytest-cov.

# Exercice 2
  
## Question 1
 
Ecrire une simple fonction ```add``` qui prend en entrée deux entiers a et b et qui renvoie leur somme. 
  Au début de la fonction, ajouter une ligne ```time.sleep(1)``` afin de simuler une fonction qui fait un calcul long et complexe.

Ecrire un décorateur ```cache``` qui viendra décorer la fonction ```add```. 
Ce décorateur enregistrera les résultats de l'appel à la fonction ```add``` dans un dictionnaire, à chaque fois que celle-ci sera appelée.
Il renverra directement le résultat contenu dans ce dictionnaire si la fonction avait déjà été appelée avec les mêmes paramètres.

## Question 2

Avec ce même décorateur, faire en sorte que les appels de ```add(a, b)``` et ```add(b, a)``` ne conduisent à appeler la fonction ```add``` qu'une seule fois.


