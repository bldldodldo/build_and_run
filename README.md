# build_and_run

Jeu de plateau : règles, implémentation en python et création de trois bots.


#### Liste des documents fournis

-  [bar.regles.pdf](bar.regles.pdf) : présentation du jeu et ses règles.
-  [bar.implementation.pdf](bar.implementation.pdf) : implémentation et mise en place d'un premier bot naïf.
-  [bar.botetapprentissage.pdf](bar.botetapprentissage.pdf) : mise en place de deux bots en apprentissage, l'un par apprentissage des coups de l'adversaire, l'autre par sélection génétique.


- - -


## Règles

Le jeu se joue sur une grille, de taille (n,p) avec n > 3 et p > 3. Les tours se divisent en deux temps :

> _Phase de déplacement : se déplacer ou détruire un mur._
  
> _Phase de construction : construire un mur (ou détruire un mur si le joueur a détruit à la phase précédente.)_

Le camp d’un joueur commençant en (1,1) [resp. (n-2,p-2)] se situe dans le coin (0,0) [resp. (n-1,p-1)]. Chaque joueur
doit défendre son camp : si quiconque, y compris lui-même, rentre dans le camp, il perd la partie. Chaque joueur
possède un `momentum` et lorsqu'il se déplace, se déplace de exactement `momentum` cases jusqu’à rencontrer un obstacle.
Quelques règles supplémentaires : 

> _Se déplacer en diagonale demande 2 de_ `momentum` _par case diagonale parcourue (partie entière inférieure de_ `momentum` _/2 cases parcourues). Ceci diminue le_ `momentum` _de 1. Se déplacer en diagonale d’une case n’est pas se
déplacer dans une direction d’une case puis dans la direction orthogonale d’une case, c’est un déplacement spécial._

> _Se déplacer verticalement ou horizontalement augmente le_ `momentum` _de 1. Si un mur bloque l’entièreté du
mouvement, le_ `momentum` _augmente de 3._

> _« Détruire un mur » se définit par « diminuer de 1 la valeur d’une case ». Une case ne peut pas avoir une valeur
inférieure à 0. Une case de valeur 0 est une case vide. Détruire ramène le momentum à la valeur 1._

> _Deux joueurs ne peuvent pas partager la même case._

> _Le premier joueur d’un tour alterne : si un tour commence par le joueur 1, le suivant par le joueur 2._

Complément d’information :

Il est interdit de construire sur les camps des joueurs. Si un joueur passe sur son propre camp, il perd. Le
`momentum` n’a pas de limite. On ne peut pas se déplacer de moins de `momentum` cases (ou de moins de la partie
entière inférieure de `momentum`/2 pour les déplacements en diagonale). La valeur d’une case n’a pas de limite.

Pour voir quelques illustrations, voir le document 

- - -


## Bots

L'implémentation du jeu ainsi que la création de trois bots pour le jeu sont présentées dans les documents listés au début du readme.
