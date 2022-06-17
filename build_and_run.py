#____________________________________________ JEU CLASSIQUE
import random
from time import sleep

def trouver(u,tab):
    """Fonction qui permet de trouver la case contenant le marqueur "u"
dans la matrice "tab"."""
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == u:
                return (i,j)
    failwith("il n'y a pas d'ennemi ici..")


from colorama import Fore

def mur(tab):
    """Fonction qui vérifie s'il existe au moins un mur sur la grille "tab"
"""
    c=0
    for i in tab:
        for j in i:
            if isinstance(j, int):
                c += j
    return not c ==0


def mov_g(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers la gauche.
Modifie la liste par effet de bord."""
    if not (y-1 >= 0 and terrain[x][y-1] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if y-1 >= 0 and terrain[x][y-1] == 0:
            terrain[x][y] = 0
            y -=1
            m -= 1
            terrain[x][y] = marq
            if m == 0:
                mom += 1
        else:
            m = 0
    return (x,y,m,mom)

def mov_d(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers la droite.
Modifie la liste par effet de bord."""
    if not (y+1 <= p-1 and terrain[x][y+1] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if y+1 <= p-1 and terrain[x][y+1] == 0:
            terrain[x][y] = 0
            y +=1
            m -= 1
            terrain[x][y] = marq
            if m == 0:
                mom += 1
        else:
            m = 0
    return (x,y,m,mom)

def mov_h(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers le haut.
Modifie la liste par effet de bord."""
    if not (x-1 >= 0 and terrain[x-1][y] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if x-1 >= 0 and terrain[x-1][y] == 0:
            terrain[x][y] = 0
            x -=1
            m -= 1
            terrain[x][y] = marq
            if m == 0:
                mom += 1
        else:
            m = 0
    return (x,y,m,mom)

def mov_b(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers le bas.
Modifie la liste par effet de bord."""
    if not (x+1 <= n-1 and terrain[x+1][y] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if x+1 <= n-1 and terrain[x+1][y] == 0:
            terrain[x][y] = 0
            x +=1
            m -= 1
            terrain[x][y] = marq
            if m == 0:
                mom += 1
        else:
            m = 0
            mom += 1
    return (x,y,m,mom)

def mov_hg(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers le haut-gauche.
Modifie la liste par effet de bord."""
    if not (m >= 2 and y-1 >= 0 and x-1 >= 0 and terrain[x-1][y-1] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if m >= 2 and y-1 >= 0 and x-1 >= 0 and terrain[x-1][y-1] == 0:
            terrain[x][y] = 0
            y -=1
            x -=1
            m -= 2
            terrain[x][y] = marq
            if m < 2:
                mom -= 1
                m = 0
        else:
            m = 0
    return (x,y,m,mom)

def mov_bg(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers le bas-gauche.
Modifie la liste par effet de bord."""
    if  not (m >= 2 and y-1 >= 0 and x+1 <= n-1 and terrain[x+1][y-1] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if m >= 2 and y-1 >= 0 and x+1 <= n-1 and terrain[x+1][y-1] == 0:
            terrain[x][y] = 0
            y -=1
            x +=1
            m -= 2
            terrain[x][y] = marq
            if m < 2:
                mom -= 1
        else:
            m = 0
    return (x,y,m,mom)

def mov_hd(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers le haut-droit.
Modifie la liste par effet de bord."""
    if not (m >= 2 and y+1 <= p-1 and x-1 >= 0 and terrain[x-1][y+1] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if m >= 2 and y+1 <= p-1 and x-1 >= 0 and terrain[x-1][y+1] == 0:
            terrain[x][y] = 0
            y +=1
            x -=1
            m -= 2
            terrain[x][y] = marq
            if m < 2:
                mom -= 1
        else:
            m = 0
    return (x,y,m,mom)

def mov_bd(x,y,terrain,m,mom,marq):
    """Fonction de déplacement vers le bas-droit.
Modifie la liste par effet de bord."""
    if not (m >= 2 and y+1 <= p-1 and x+1 <= n-1 and terrain[x+1][y+1] == 0) and m == mom:
        m = 0
        mom += 3
    while m > 0:
        if m >= 2 and y+1 <= p-1 and x+1 <= n-1 and terrain[x+1][y+1] == 0:
            terrain[x][y] = 0
            y +=1
            x +=1
            m -= 2
            terrain[x][y] = marq
            if m < 2:
                mom -= 1
        else:
            m = 0
    return (x,y,m,mom)

def del_h(x,y,terrain):
    """Fonction qui supprime un mur (réduit la valeur de la case de 1) en haut.
Ne vérifie pas si les coordonnées données sont correctes
et si la case possède au moins un mur."""
    terrain[x-1][y] -= 1
    mom = 1
    deli = 1
    return (x,y,mom,deli)

def del_g(x,y,terrain):
    """Fonction qui supprime un mur (réduit la valeur de la case de 1) à gauche.
Ne vérifie pas si les coordonnées données sont correctes
et si la case possède au moins un mur."""
    terrain[x][y-1] -= 1
    mom = 1
    deli = 1
    return (x,y,mom,deli)



def del_d(x,y,terrain):
    """Fonction qui supprime un mur (réduit la valeur de la case de 1) à droite.
Ne vérifie pas si les coordonnées données sont correctes
et si la case possède au moins un mur."""
    terrain[x][y+1] -= 1
    mom = 1
    deli = 1
    return (x,y,mom,deli)

def del_b(x,y,terrain):
    """Fonction qui supprime un mur (réduit la valeur de la case de 1) en bas.
Ne vérifie pas si les coordonnées données sont correctes
et si la case possède au moins un mur."""
    terrain[x+1][y] -= 1
    mom = 1
    deli = 1
    return (x,y,mom,deli)

def bot_1(x,y,terrain,tour,mom,marq,deli,obj, ennemi = "j1"):
    """Fonction de coup du bot.
x,y sont les coordonnées du marqueur (position du bot).
mom est le momentum du bot.
marq le marqueur associée (par ex. "j1")
deli permet de savoir si le coup joué à la phase de déplacement est une destruction
(permet de détruire aussi à la phase de construction)
obj permet de savoir quel est l'objectif du bot (où il a commencé)
ennemi permet de trouver l'ennemi à l'aide de la fonction "trouver"
C'est bot_1 qui se charge de vérifier la validité des coups.
"""
    global n
    n = len(terrain)
    global p
    p = len(terrain[0])
    tourbi = tour%2
    if obj == 0:
        if tourbi == 0:
            
            deli = 0 
            m = mom
            #solution1
            if y-1 >= 0 and terrain[x][y-1] == 0:
                (x,y,m,mom) = mov_g(x,y,terrain,m,mom,marq)
            elif x-1 >= 0 and terrain[x-1][y] == 0:
                (x,y,m,mom) = mov_h(x,y,terrain,m,mom,marq)
            #diag
            elif m >= 2 and y-1 >= 0 and x-1 >= 0 and terrain[x-1][y-1] == 0:
                (x,y,m,mom) = mov_hg(x,y,terrain,m,mom,marq)
            elif m >= 2 and y-1 >= 0 and x+1 <= n-1 and terrain[x+1][y-1] == 0:
                (x,y,m,mom) = mov_bg(x,y,terrain,m,mom,marq)
            elif m >= 2 and y+1 <= p-1 and x-1 >= 0 and terrain[x-1][y+1] == 0:
                (x,y,m,mom) = mov_hd(x,y,terrain,m,mom,marq)
            #panic del
            elif x-1 >= 0 and isinstance(terrain[x-1][y],int) and terrain[x-1][y] > 0:
                (x,y,mom,deli) = del_h(x,y,terrain)
            elif y-1 >= 0 and isinstance(terrain[x][y-1],int) and terrain[x][y-1] > 0:
                (x,y,mom,deli) = del_g(x,y,terrain)
            #panicpanic recul
            elif x+1 <= n-1 and terrain[x+1][y] == 0:
                (x,y,m,mom) = mov_b(x,y,terrain,m,mom,marq)
            elif y+1 <= p-1 and terrain[x][y+1] == 0:
                (x,y,m,mom) = mov_d(x,y,terrain,m,mom,marq)
# SUPPRIMER-MOV POUR OBJ 0            
            elif x+1 <= n-1 and isinstance(terrain[x+1][y],int) and terrain[x+1][y] > 0:
                (x,y,mom,deli) = del_b(x,y,terrain)
            elif y+1 <= p-1 and isinstance(terrain[x][y+1],int) and terrain[x][y+1] > 0:
                (x,y,mom,deli) = del_d(x,y,terrain)
            #le return
            return (x,y,mom,deli)
# CON OBJ 0
        elif tourbi == 1:
            if deli == 0:
                (ex, ey) = trouver(ennemi, terrain)
                if ey+1 <= p-1 and isinstance(terrain[ex][ey+1], int) and (ex,ey+1)!=(0,0) and (ex,ey+1)!=(n-1,p-1):
                    terrain[ex][ey+1] += 1
                elif ex+1 <= n-1 and isinstance(terrain[ex+1][ey], int) and (ex+1,ey)!=(0,0) and (ex+1,ey)!=(n-1,p-1):
                    terrain[ex+1][ey] += 1
                elif ey - 1 >= 0 and isinstance(terrain[ex][ey-1], int) and (ex,ey-1)!=(0,0) and (ex,ey-1)!=(n-1,p-1):
                    terrain[ex][ey-1] += 1
                elif ex-1 >= 0 and isinstance(terrain[ex-1][ey], int) and (ex-1,ey)!=(0,0) and (ex-1,ey)!=(n-1,p-1):
                    terrain[ex-1][ey] += 1
                return (x,y,mom,deli)
            else:
                (ex, ey) = trouver(ennemi, terrain)
                if x-1 >= 0 and isinstance(terrain[x-1][y],int) and terrain[x-1][y] > 0:
                    terrain[x-1][y] -= 1
                    mom = 1
                    deli = 1
                elif y-1 >= 0 and isinstance(terrain[x][y-1],int) and terrain[x][y-1] > 0:
                    terrain[x][y-1] -= 1
                    mom = 1
                    deli = 1
                elif x+1 <= n-1 and isinstance(terrain[x+1][y],int) and terrain[x+1][y] > 0:
                    terrain[x+1][y] -= 1
                    mom = 1
                    deli = 1
                elif y+1 <= p-1 and isinstance(terrain[x][y+1],int) and terrain[x][y+1] > 0:
                    terrain[x][y+1] -= 1
                    mom = 1
                    deli = 1
                elif ex+1 <= n-1 and isinstance(terrain[ex+1][ey], int) and (ex+1,ey)!=(0,0) and (ex+1,ey)!=(n-1,p-1):
                    terrain[ex+1][ey] += 1
                elif ey+1 <= p-1 and isinstance(terrain[ex][ey+1], int) and (ex,ey+1)!=(0,0) and (ex,ey+1)!=(n-1,p-1):
                    terrain[ex][ey+1] += 1
                elif ey-1 >= 0 and isinstance(terrain[ex][ey-1], int) and (ex,ey-1)!=(0,0) and (ex,ey-1)!=(n-1,p-1):
                    terrain[ex][ey-1] += 1
                elif ex-1 >= 0 and isinstance(terrain[ex-1][ey], int) and (ex-1,ey)!=(0,0) and (ex-1,ey)!=(n-1,p-1):
                    terrain[ex-1][ey] += 1
                #le return
                return (x,y,mom,deli)
                
    elif obj == 1:
        if tourbi == 0:
            
            deli = 0 
            m = mom
            #sol 1
            if y+1 <= p-1 and terrain[x][y+1] == 0:
                (x,y,m,mom) = mov_d(x,y,terrain,m,mom,marq)
            elif x+1 <= n-1 and terrain[x+1][y] == 0:
                (x,y,m,mom) = mov_b(x,y,terrain,m,mom,marq)
            #diag
            elif m >= 2 and y+1 <= p-1 and x+1 <= n-1 and terrain[x+1][y+1] == 0:
                (x,y,m,mom) = mov_bd(x,y,terrain,m,mom,marq)
            elif m >= 2 and y-1 >= 0 and x+1 <= n-1 and terrain[x+1][y-1] == 0:
                (x,y,m,mom) = mov_bg(x,y,terrain,m,mom,marq)
            elif m >= 2 and y+1 <= p-1 and x-1 >= 0 and terrain[x-1][y+1] == 0:
                (x,y,m,mom) = mov_hd(x,y,terrain,m,mom,marq)
            #panic del
            elif x+1 <= n-1 and isinstance(terrain[x+1][y],int) and terrain[x+1][y] > 0:
                (x,y,mom,deli) = del_b(x,y,terrain)
            elif y+1 <= p-1 and isinstance(terrain[x][y+1],int) and terrain[x][y+1] > 0:
                (x,y,mom,deli) = del_d(x,y,terrain)
            #panicpanic recul
            elif x-1 >= 0 and terrain[x-1][y] == 0:
                (x,y,m,mom) = mov_g(x,y,terrain,m,mom,marq)
            elif y-1 >= 0 and terrain[x][y-1] == 0:
                (x,y,m,mom) = mov_h(x,y,terrain,m,mom,marq)
#SUPPRIMER-MOV OBJ 1
            elif x-1 >= 0 and isinstance(terrain[x-1][y],int) and terrain[x-1][y] > 0:
                (x,y,mom,deli) = del_h(x,y,terrain)
            elif y-1 >= 0 and isinstance(terrain[x][y-1],int) and terrain[x][y-1] > 0:
                (x,y,mom,deli) = del_g(x,y,terrain)
            return (x,y,mom,deli)
        
        
        elif tourbi == 1:
            if deli == 0:
                (ex, ey) = trouver(ennemi, terrain)
                if ey - 1 >= 0 and isinstance(terrain[ex][ey-1], int) and (ex,ey-1)!=(0,0) and (ex,ey-1)!=(n-1,p-1):
                    terrain[ex][ey-1] += 1
                elif ex-1 >= 0 and isinstance(terrain[ex-1][ey], int) and (ex-1,ey)!=(0,0) and (ex-1,ey)!=(n-1,p-1):
                    terrain[ex-1][ey] += 1
                elif ex+1 <= n-1 and isinstance(terrain[ex+1][ey], int) and (ex+1,ey)!=(0,0) and (ex+1,ey)!=(n-1,p-1):
                    terrain[ex+1][ey] += 1
                elif ey+1 <= p-1 and isinstance(terrain[ex][ey+1], int) and (ex,ey+1)!=(0,0) and (ex,ey+1)!=(n-1,p-1):
                    terrain[ex][ey+1] += 1
                return (x,y,mom,deli)
            else:
                (ex, ey) = trouver(ennemi, terrain)
                if x+1 <= n-1 and isinstance(terrain[x+1][y],int) and terrain[x+1][y] > 0:
                    terrain[x+1][y] -= 1
                    mom = 1
                    deli = 1
                elif y+1 <= p-1 and isinstance(terrain[x][y+1],int) and terrain[x][y+1] > 0:
                    terrain[x][y+1] -= 1
                    mom = 1
                    deli = 1
                elif x-1 >= 0 and isinstance(terrain[x-1][y],int) and terrain[x-1][y] > 0:
                    terrain[x-1][y] -= 1
                    mom = 1
                    deli = 1
                elif y-1 >= 0 and isinstance(terrain[x][y-1],int) and terrain[x][y-1] > 0:
                    terrain[x][y-1] -= 1
                    mom = 1
                    deli = 1
                elif ey - 1 >= 0 and isinstance(terrain[ex][ey-1], int) and (ex,ey-1)!=(0,0) and (ex,ey-1)!=(n-1,p-1):
                    terrain[ex][ey-1] += 1
                elif ex-1 >= 0 and isinstance(terrain[ex-1][ey], int) and (ex-1,ey)!=(0,0) and (ex-1,ey)!=(n-1,p-1):
                    terrain[ex-1][ey] += 1
                elif ex+1 <= n-1 and isinstance(terrain[ex+1][ey], int) and (ex+1,ey)!=(0,0) and (ex+1,ey)!=(n-1,p-1):
                    terrain[ex+1][ey] += 1
                elif ey+1 <= p-1 and isinstance(terrain[ex][ey+1], int) and (ex,ey+1)!=(0,0) and (ex,ey+1)!=(n-1,p-1):
                    terrain[ex][ey+1] += 1
                return (x,y,mom,deli)
                
                

def joueur(x,y,terrain,tour,mom,marq,deli, obj = 0, ennemi = "j1"):
    """
Fonction qui permet à un joueur humain d'intéragir avec le jeu.
C'est la difficulté d'offrir une interactivité agréable au joueur qui engendre
l'utilisation de nombreuses boucles "while" imbriquées.
x,y sont les coordonnées du marqueur (position du bot).
mom est le momentum du bot.
marq le marqueur associée (par ex. "j1")
deli permet de savoir si le coup joué à la phase de déplacement est une destruction
(permet de détruire aussi à la phase de construction)
obj permet de savoir quel est l'objectif du bot (où il a commencé)
ennemi permet de trouver l'ennemi à l'aide de la fonction "trouver"
"""
    n = len(terrain)
    p = len(terrain[0])
    tourbi = tour%2
    if tourbi == 0:
        r = 1
        while r != 0:
            ask = input("Détruire ou se déplacer ? (DET,MOV)(detruire reset le mom) : ")
            if ask == "MOV":
                r = 0
                inp = 1
                while inp != 0:
                    inp = input("direction de deplacement (H, B, G, D, HG, HD, BG, BD) :")
                    
                    if inp == "D":
                        m = mom
                        while m > 0:
                            if y+1 <= p-1 and terrain[x][y+1] == 0:
                                terrain[x][y] = 0
                                y +=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            else:
                                inp = 0
                                mom += 1
                                m = 0
                                
                    elif inp == "G":
                        m = mom
                        while m > 0:
                            if y-1 >= 0 and terrain[x][y-1] == 0:
                                terrain[x][y] = 0
                                y -=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            else:
                                inp = 0
                                mom += 1
                                m = 0
                    
                    elif inp == "B":
                        m = mom
                        while m > 0:
                            if x+1 <= n-1 and terrain[x+1][y] == 0:
                                terrain[x][y] = 0
                                x +=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m =0
                            else:
                                inp = 0
                                mom += 1
                                m = 0
                                
                    elif inp == "H":
                        m = mom
                        while m > 0:
                            if x-1 >= 0 and terrain[x-1][y] == 0:
                                terrain[x][y] = 0
                                x -=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            else:
                                inp = 0
                                mom += 1
                                m = 0
                                
                    elif inp == "HD":
                        m = mom
                        while m > 0:
                            if x-1 >= 0 and y+1 <= p-1 and terrain[x-1][y+1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x -=1
                                y += 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >=2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                inp = 0
                                mom -= 1
                                m = 0
        
                    elif inp == "BD":
                        m = mom
                        while m > 0:
                            if x+1 <= n-1 and y+1 <= p-1 and terrain[x+1][y+1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x +=1
                                y += 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >=2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                inp = 0
                                mom -= 1
                                m = 0
                                
                    elif inp == "BG":
                        m = mom
                        while m > 0:
                            if x+1 <= n-1 and y-1 >= 0 and terrain[x+1][y-1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x +=1
                                y -= 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >=2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                inp = 0
                                mom -= 1
                                m = 0
        
                    elif inp == "HG":
                        m = mom
                        while m > 0:
                            if x-1 >= 0 and y-1 >= 0 and terrain[x-1][y-1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x -=1
                                y -= 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >= 2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                inp = 0
                                mom -= 1
                                m = 0
                return (x,y,mom,deli)
            elif ask == "DET" and mur(terrain):
                r = 1
                while True:
                    print("donnez les coordonnees (x,y) du mur à détruire :")
                    test =1
                    while not test == 0:
                        try :
                            test = 0
                            xu = int(input("x :"))
                            yu = int(input("y :"))
                            if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0) or terrain[yu][xu] <= 0:
                                test = 1
                                print("les coordonnées sont incorrectes.")
                        except:
                            print("il faut donner des entiers")
                            test = 1
                        
                    if isinstance(terrain[yu][xu], int):
                        terrain[yu][xu] -= 1
                        mom = 1
                        return(x,y,mom,1)
                    else:
                        print("il y a un joueur ici..")
            elif ask == "DET":
                print("il n'y a aucun mur à détruire.")
            else :
                print("commande inconnue")
                
    elif deli ==1:
        deli = 0
        r = 1
        while r != 0:
            ask = input("Détruire ou construire ? (DET,CON) : ")
            if ask == "CON":
                while True:
                    print("donnez les coordonnees (x,y) du mur à construire :")
                    test =1
                    while not test == 0:
                        try :
                            test = 0
                            xu = int(input("x :"))
                            yu = int(input("y :"))
                            if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0):
                                test = 1
                                print("les coordonnées sont incorrectes.")
                        except:
                            print("il faut donner des entiers")
                            test = 1
                        
                    if isinstance(terrain[yu][xu], int):
                        terrain[yu][xu] += 1
                        return(x,y,mom,deli)
                    else:
                        print("il y a un joueur ici..")
            elif ask == "DET" and mur(terrain):
                while True:
                    print("donnez les coordonnees (x,y) du mur à détruire :")
                    test =1
                    while not test == 0:
                        try :
                            test = 0
                            xu = int(input("x :"))
                            yu = int(input("y :"))
                            if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0) or terrain[yu][xu] <= 0:
                                test = 1
                                print("les coordonnées sont incorrectes.")
                        except:
                            print("il faut donner des entiers")
                            test = 1
                        
                    if isinstance(terrain[yu][xu], int):
                        terrain[yu][xu] -= 1
                        mom = 1
                        return(x,y,mom,deli)
                    else:
                        print("il y a un joueur ici..")
            elif ask == "DET":
                print("il n'y a aucun mur à détruire.")
            else :
                print("commande inconnue")
                
                
                
    else:
        deli = 0
        while True:
            print("donnez les coordonnees (x,y) du mur à construire :")
            test =1
            while not test == 0:
                try :
                    test = 0
                    xu = int(input("x :"))
                    yu = int(input("y :"))
                    if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0):
                        test = 1
                        print("les coordonnées sont incorrectes.")
                except:
                    print("il faut donner des entiers")
                    test = 1
                
            if isinstance(terrain[yu][xu], int):
                terrain[yu][xu] += 1
                return(x,y,mom,deli)
            else:
                print("il y a un joueur ici..")

def print_terrain3(ter,col2,col1):
    """fonction de print du terrain. Obsolète mais conservée si besoin de revenir en arrière
sur l'affichage. N'impacte pas le fonctionnement du programme."""
    res = "\t"
    for i in range(len(ter[0])):
        res += str(i) + "\t"
    res += "\n\n"
    for x in range(len(ter)):
        res += str(x) + "\t"
        for y in range(len(ter[x])):
            res += str(ter[x][y]) + "\t"
        res += "\n\n"
    print(res)


def print_terrain2(ter, col2, col1):
    """fonction de print du terrain. Obsolète mais conservée si besoin de revenir en arrière
sur l'affichage. N'impacte pas le fonctionnement du programme."""
    print("", end = "      ")
    for i in range(len(ter[0])):
        print(i, end = "  ")
    print()
    print()
    print()
    for i in range(len(ter)):
        print(i, end = "     ")
        for j in range(len(ter[i])):
            if ter[i][j] == "j1":
                print(col1 + ter[i][j], end = "  " + Fore.BLACK)
            elif ter[i][j] == "j2":
                print(col2 + ter[i][j], end = "  " + Fore.BLACK)
            else:
                print(ter[i][j], end = "  ")
        print()
        print()



def print_terrain(ter, col2, col1):
    """Fonction de print du terrain.
Colorama et Fore permettent de colorer l'interpréteur et donc l'affichage du jeu.
"""
    n = len(ter)
    p = len(ter[0])
    print("", end = "\t")
    for i in range(len(ter[0])):
        print(i, end = "\t")
    print()
    print()
    print()
    for i in range(len(ter)):
        print(i, end = "\t")
        for j in range(len(ter[i])):
            if ter[i][j] == "j1":
                print(col1 + ter[i][j], end = "\t" + Fore.BLACK)
            elif ter[i][j] == "j2":
                print(col2 + ter[i][j], end = "\t" + Fore.BLACK)
            elif (i,j) == (0,0) or (i,j) == ((n-1),(p-1)):
                print(Fore.RED + "௦" + Fore.BLACK, end = "\t")
            elif ter[i][j] == 0:
                print("▫", end = "\t")
            else:
                print(Fore.BLUE + str(ter[i][j]) + Fore.BLACK, end = "\t")
        print()
        print()

def partie(n,p,j1,j2):
    """
La fonction partie permet de lancer une partie entre deux "fonctions joueurs" (ex. bot_1 ou joueur)
n,p est la taille du terrain pour la partie.
"""
    terrain = [[0 for i in range(n)] for j in range(p)]
    x1,y1 = 1,1
    x2,y2 = (p-2),(n-2)
    tour = 0
    premierjoueur = 0
    mom1,mom2 = 1,1
    del1,del2 = 0,0
    terrain[x1][y1] = "j1"
    terrain[x2][y2] = "j2"
    while (x1,y1) != ((p-1),(n-1)) and (x2,y2) != (0,0):
        if premierjoueur <= 1:
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.YELLOW + "joueur1: ( de momentum =", mom1, ")" + Fore.BLACK)
            (x1,y1,mom1,del1) = j1(x1,y1,terrain,tour,mom1,"j1",del1,1, "j2")
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.GREEN + "joueur2: ( de momentum =", mom2, ")" + Fore.BLACK)
            (x2, y2,mom2,del2) = j2(x2,y2,terrain,tour,mom2, "j2",del2,0)
            tour = (tour+1)
            premierjoueur +=1
        else:
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.GREEN + "joueur2: ( de momentum =", mom2, ")" + Fore.BLACK)
            (x2,y2,mom2,del2) = j2(x2,y2,terrain,tour,mom2,"j2",del2,0)
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.YELLOW + "joueur1: ( de momentum =", mom1, ")" + Fore.BLACK)
            (x1, y1,mom1,del1) = j1(x1,y1,terrain,tour,mom1, "j1",del1,1, "j2")
            tour = (tour+1)
            premierjoueur += 1
            if premierjoueur >= 4:
                premierjoueur = 0
            
    if premierjoueur <= 2:
        if (x1,y1) == (p-1,n-1) or (x2, y2) == (p-1, n-1):
            print("le joueur 1 a gagné")
        else:
            print("le joueur 2 a gagné")
    else:
        if (x2,y2) == (0,0) or (x1,y1) == (0,0):
            print("le joueur 2 a gagné")
        else:
            print("le joueur 1 a gagné")
            
    
#partie(10,4,bot_1,bot_1)
                
#___________________________________________________________________________________________________________________________________________________
#____________________________________________ FONCTION POUR L'APPRENTISSAGE NAIF

import pickle
import build_and_run as bar
import colorama
from colorama import Fore
from time import sleep
import copy
new_freq = [["H",0],["B",0],["G",0],["D",0],["HG",0],["BG",0],["HD",0],["BD",0]]

#____________________________________________ FONCTION DE TRI (TRI RAPIDE)



def tri(tab, d, f):
    clé = tab[d]
    gauche = d
    droite = f
    while droite > gauche:
        while clé[1] > tab[gauche][1]:
            gauche += 1
        while clé[1] < tab[droite][1]:
            droite -= 1
        temp = tab[gauche]
        tab[gauche] = tab[droite]
        tab[droite] = temp
        if tab[gauche][1] == tab[droite][1]:
            gauche += 1
    return droite

def trirap(tab, d, f):
    if d < f:
        pos = tri(tab, d, f)
        trirap(tab, d, pos-1)
        trirap(tab, pos+1, f)
    return tab

def triliste(tab):
    return trirap(tab, 0, len(tab)-1)

#____________________________________________ FONCTIONS DE GESTION DU FICHIER DE STOCKAGE D'INFORMATIONS DU BOT EN APPRENTISSAGE

def ecrire(tab):
    with open("tableau", "wb") as save:   #Pickling
        pickle.dump(tab, save)
        
def recup():
    with open("tableau", "rb") as save:   #Unpickling
        b = pickle.load(save)
        return b

#____________________________________________ 

def symetrique(coup):
    """Fonction permettant de trouver le symétrique d'un coup.
(symétrie centrale de centre le centre du terrain)
ex. "H" donne "B"
"HD" donne "BG"
"""
    if coup == "H":
        return "B"
    elif coup == "B":
        return "H"
    elif coup == "D":
        return "G"
    elif coup == "G":
        return "D"
    elif coup == "HG":
        return "BD"
    elif coup == "HD":
        return "BG"
    elif coup == "BD":
        return "HG"
    elif coup == "BG":
        return "HD"

#____________________________________________
    
def trouver_coup_commun(lst,k):
    """Fonction qui permet de trouver le coup le plus joué dans la liste de liste."""
    triee = triliste(lst)
    m = len(triee)
    return triee[m - k - 1]

def bot_coup_mov(tab,n):
    return trouver_coup_commun(tab[n])

def apprendre_coup(coup, tour, tab):
    """Fonction qui permet de retenir le coup donné en argument "coup" """
    while tour > (len(tab) - 1):
        lst = copy.deepcopy(new_freq)
        tab.append(lst)
    for i in tab[tour]:
        if i[0] == coup:
            i[1] += 1

def nouveau_coup(tab):
    tab.append(new_freq.copy())

def coup_possible_obsolète(coup_lst,x,y,terrain,m):
    """Fonction obsolète qui vérifie si la situation respecte certaines conditions."""
    coup = coup_lst[0]
    if coup_lst[1] == 0:
        return False
    elif coup == "H":
        return x-1 >= 0 and terrain[x-1][y] == 0
    elif coup == "B":
        return x+1 <= n-1 and terrain[x+1][y] == 0
    elif coup == "G":
        return y-1 >= 0 and terrain[x][y-1] == 0
    elif coup == "D":
        return y+1 <= p-1 and terrain[x][y+1] == 0
    elif coup == "HG":
        return m >= 2 and y-1 >= 0 and x-1 >= 0 and terrain[x-1][y-1] == 0
    elif coup == "HD":
        return m >= 2 and y+1 <= p-1 and x-1 >= 0 and terrain[x-1][y+1] == 0
    elif coup == "BG":
        return m >= 2 and y-1 >= 0 and x+1 <= n-1 and terrain[x+1][y-1] == 0
    elif coup == "BD":
        return m >= 2 and y+1 <= p-1 and x+1 <= n-1 and terrain[x+1][y+1] == 0
    
def coup_possible(coup_lst,x,y,terrain,m):
    """Permet de trouver si un coup est possible ou non. Renvoie un booléen."""
    coup = coup_lst[0]
    if coup == "HG" and y-1 >= 0 and x-1 >= 0 and terrain[x-1][y-1]:
        return m >= 2
    elif coup == "HD" and y+1 <= p-1 and x-1 >= 0 and terrain[x-1][y+1]:
        return m >= 2
    elif coup == "BG" and y-1 >= 0 and x+1 <= n-1 and terrain[x+1][y-1]:
        return m >= 2
    elif coup == "BD" and y+1 <= p-1 and x+1 <= n-1 and terrain[x+1][y+1]:
        return m >= 2
    else:
        return True
#____________________________________________
    
def filtrage(coup, x, y, terrain, m, mom, marq):
    """Remplace un filtrage."""
    if coup[0] == "H":
        return mov_h(x,y,terrain,m,mom,marq)
    elif coup[0] == "B":
        return mov_b(x,y,terrain,m,mom,marq)
    elif coup[0] == "G":
        return mov_g(x,y,terrain,m,mom,marq)
    elif coup[0] == "D":
        return mov_d(x,y,terrain,m,mom,marq)
    elif coup[0] == "HG":
        return mov_hg(x,y,terrain,m,mom,marq)
    elif coup[0] == "HD":
        return mov_hd(x,y,terrain,m,mom,marq)
    elif coup[0] == "BG":
        return mov_bg(x,y,terrain,m,mom,marq)
    elif coup[0] == "BD":
        return mov_hg(x,y,terrain,m,mom,marq)
    elif coup[0] == "DET":
        return detruire_bot(x,y,terrain,m,mom,marq)
    else:
        print("il ne se passe rien")
        return (x,y,m,mom)

#____________________________________________
    
def bot_coup(x,y,terrain,tour,mom,marq,deli, obj = 0, ennemi = "j1"):
    """Fonction qui permet de jouer un tour du bot.
x,y sont les coordonnées du marqueur (position du bot).
mom est le momentum du bot.
tour permet de savoir quel est le numéro du tour qui est joué. Ceci
permet de mettre à jour correctement le tableau des données de ce qu'apprend le coup.
marq le marqueur associée (par ex. "j1")
deli permet de savoir si le coup joué à la phase de déplacement est une destruction
(permet de détruire aussi à la phase de construction)
obj permet de savoir quel est l'objectif du bot (où il a commencé)
ennemi permet de trouver l'ennemi à l'aide de la fonction "trouver"
"""
    global n
    n = len(terrain)
    global p
    p = len(terrain[0])
    tab = recup()
    tourbi = tour % 2
    tourdiv = tour // 2
    m = mom
    if tourbi == 0:
        if tourdiv > (len(tab) - 1):
            return bot_1(x,y,terrain,tour,mom, marq , deli , obj , ennemi)
        else:
            i = 0
            cou = trouver_coup_commun(tab[tourdiv], i)
            while cou[1] == 0 and not (coup_possible(cou, m)) and i < (len(tab)) :
                cou = trouver_coup_commun(tab[tourdiv], i)
                i += 1
                
            if i >= len(tab) and not coup_possible(cou, m):
                return bot_1(x,y,terrain,tour,mom, marq , deli , obj , ennemi)
            else:
                (x,y,m,mom) = filtrage(cou, x, y, terrain, m, mom, marq)
                return (x,y,mom,deli)
                
    elif tourbi == 1:
        return bot_1(x,y,terrain,tour,mom, marq , deli , obj , ennemi)
    
def bot_apprendre(x,y,terrain,tour,mom,marq,deli, obj = 0, ennemi = "j1"):
    """fonction globale qui permet de faire jouer un joueur réel et de faire apprendre au bot qui apprend.
x,y sont les coordonnées du marqueur (position du bot).
tour permet de savoir quel est le numéro du tour qui est joué. Ceci
permet de mettre à jour correctement le tableau des données de ce qu'apprend le coup.
mom est le momentum du bot.
marq le marqueur associée (par ex. "j1")
deli permet de savoir si le coup joué à la phase de déplacement est une destruction
(permet de détruire aussi à la phase de construction)
obj permet de savoir quel est l'objectif du bot (où il a commencé)
ennemi permet de trouver l'ennemi à l'aide de la fonction "trouver"
"""
    n = len(terrain)
    p = len(terrain[0])
    tourbi = tour%2
    tourv = tour // 2
    if tourbi == 0:
        r = 1
        while r != 0:
            ask = input("Détruire ou se déplacer ? (DET,MOV)(detruire reset le mom) : ")
            if ask == "MOV":
                r = 0
                inp = 1
                while inp != 0:
                    inp = input("direction de deplacement (H, B, G, D, HG, HD, BG, BD) :")
                    
                    if inp == "D":
                        m = mom
                        while m > 0:
                            if y+1 <= p-1 and terrain[x][y+1] == 0:
                                terrain[x][y] = 0
                                y +=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom += 1
                                m = 0
                                
                    elif inp == "G":
                        m = mom
                        while m > 0:
                            if y-1 >= 0 and terrain[x][y-1] == 0:
                                terrain[x][y] = 0
                                y -=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom += 1
                                m = 0
                    
                    elif inp == "B":
                        m = mom
                        while m > 0:
                            if x+1 <= n-1 and terrain[x+1][y] == 0:
                                terrain[x][y] = 0
                                x +=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m =0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom += 1
                                m = 0
                                
                    elif inp == "H":
                        m = mom
                        while m > 0:
                            if x-1 >= 0 and terrain[x-1][y] == 0:
                                terrain[x][y] = 0
                                x -=1
                                m -= 1
                                terrain[x][y] = marq
                                if m == 0:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 1
                            elif m == mom:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom += 1
                                m = 0
                                
                    elif inp == "HD":
                        m = mom
                        while m > 0:
                            if x-1 >= 0 and y+1 <= p-1 and terrain[x-1][y+1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x -=1
                                y += 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >=2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom -= 1
                                m = 0
        
                    elif inp == "BD":
                        m = mom
                        while m > 0:
                            if x+1 <= n-1 and y+1 <= p-1 and terrain[x+1][y+1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x +=1
                                y += 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >=2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom -= 1
                                m = 0
                                
                    elif inp == "BG":
                        m = mom
                        while m > 0:
                            if x+1 <= n-1 and y-1 >= 0 and terrain[x+1][y-1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x +=1
                                y -= 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >=2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m == mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom -= 1
                                m = 0
        
                    elif inp == "HG":
                        m = mom
                        while m > 0:
                            if x-1 >= 0 and y-1 >= 0 and terrain[x-1][y-1] == 0 and m >= 2:
                                terrain[x][y] = 0
                                x -=1
                                y -= 1
                                m -= 2
                                terrain[x][y] = marq
                                if m <= 1:
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom -= 1
                                    m = 0
                            elif m == mom and m >= 2:
                                conf = input("vous ne vous déplacerez pas, êtes-vous sûr ? (OUI, NON)")
                                if conf == "OUI":
                                    apprendre_coup(symetrique(inp), tourv, tab)
                                    inp = 0
                                    mom += 3
                                    m = 0
                                else:
                                    inp = 1
                                    m = 0
                            elif m==mom and m < 2:
                                print("pas assez de momentum")
                                inp = 1
                                m = 0
                            else:
                                apprendre_coup(symetrique(inp), tourv, tab)
                                inp = 0
                                mom -= 1
                                m = 0
                return (x,y,mom,deli)
            elif ask == "DET" and mur(terrain):
                r = 1
                while True:
                    print("donnez les coordonnees (x,y) du mur à détruire :")
                    test =1
                    while not test == 0:
                        try :
                            test = 0
                            xu = int(input("x :"))
                            yu = int(input("y :"))
                            if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0) or terrain[yu][xu] <= 0:
                                test = 1
                                print("les coordonnées sont incorrectes.")
                        except:
                            print("il faut donner des entiers")
                            test = 1
                        
                    if isinstance(terrain[yu][xu], int):
                        terrain[yu][xu] -= 1
                        mom = 1
                        return(x,y,mom,1)
                    else:
                        print("il y a un joueur ici..")
            elif ask == "DET":
                print("il n'y a aucun mur à détruire.")
            else :
                print("commande inconnue")
                
    elif deli ==1:
        deli = 0
        r = 1
        while r != 0:
            ask = input("Détruire ou construire ? (DET,CON) : ")
            if ask == "CON":
                while True:
                    print("donnez les coordonnees (x,y) du mur à construire :")
                    test =1
                    while not test == 0:
                        try :
                            test = 0
                            xu = int(input("x :"))
                            yu = int(input("y :"))
                            if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0):
                                test = 1
                                print("les coordonnées sont incorrectes.")
                        except:
                            print("il faut donner des entiers")
                            test = 1
                        
                    if isinstance(terrain[yu][xu], int):
                        terrain[yu][xu] += 1
                        return(x,y,mom,deli)
                    else:
                        print("il y a un joueur ici..")
            elif ask == "DET" and mur(terrain):
                while True:
                    print("donnez les coordonnees (x,y) du mur à détruire :")
                    test =1
                    while not test == 0:
                        try :
                            test = 0
                            xu = int(input("x :"))
                            yu = int(input("y :"))
                            if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0) or terrain[yu][xu] <= 0:
                                test = 1
                                print("les coordonnées sont incorrectes.")
                        except:
                            print("il faut donner des entiers")
                            test = 1
                        
                    if isinstance(terrain[yu][xu], int):
                        terrain[yu][xu] -= 1
                        mom = 1
                        return(x,y,mom,deli)
                    else:
                        print("il y a un joueur ici..")
            elif ask == "DET":
                print("il n'y a aucun mur à détruire.")
            else :
                print("commande inconnue")
                
                
                
    else:
        deli = 0
        while True:
            print("donnez les coordonnees (x,y) du mur à construire :")
            test =1
            while not test == 0:
                try :
                    test = 0
                    xu = int(input("x :"))
                    yu = int(input("y :"))
                    if xu >= p or xu < 0 or yu >= n or yu < 0 or (xu == p-1 and yu == n-1) or (xu,yu) == (0,0):
                        test = 1
                        print("les coordonnées sont incorrectes.")
                except:
                    print("il faut donner des entiers")
                    test = 1
                
            if isinstance(terrain[yu][xu], int):
                terrain[yu][xu] += 1
                return(x,y,mom,deli)
            else:
                print("il y a un joueur ici..")
                

def partie_learning(n, p, j1 = bot_apprendre, j2 = bot_coup):
    """Fonction analogue à la fonction "partie" qui permet de faire jouer
correctement les fonctions bot_coup et bot_apprentissage""" 
    global tab
    tab = recup()
    terrain = [[0 for i in range(n)] for j in range(p)]
    x1,y1 = 1,1
    x2,y2 = (p-2),(n-2)
    tour = 0
    premierjoueur = 0
    mom1,mom2 = 1,1
    del1,del2 = 0,0
    terrain[x1][y1] = "j1"
    terrain[x2][y2] = "j2"
    while (x1,y1) != ((p-1),(n-1)) and (x2,y2) != (0,0) and (x1,y1) != (0,0) and (x2,y2) != ((p-1),(n-1)):
        if premierjoueur <= 1:
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.YELLOW + "joueur1: ( de momentum =", mom1, ")" + Fore.BLACK)
            (x1,y1,mom1,del1) = j1(x1,y1,terrain,tour,mom1,"j1",del1,1, "j2")
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.GREEN + "joueur2: ( de momentum =", mom2, ")" + Fore.BLACK)
            (x2, y2,mom2,del2) = j2(x2,y2,terrain,tour,mom2, "j2",del2,0)
            tour = (tour+1)
            premierjoueur +=1
        else:
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.GREEN + "joueur2: ( de momentum =", mom2, ")" + Fore.BLACK)
            (x2, y2, mom2, del2) = j2(x2,y2,terrain,tour,mom2,"j2",del2,0)
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(1)
            print(Fore.YELLOW + "joueur1: ( de momentum =", mom1, ")" + Fore.BLACK)
            (x1, y1, mom1, del1) = j1(x1,y1,terrain,tour,mom1, "j1",del1,1, "j2")
            tour = (tour+1)
            premierjoueur +=1
            if premierjoueur >= 4:
                premierjoueur = 0
            
    if premierjoueur <= 2:
        if (x1,y1) == (p-1,n-1) or (x2, y2) == (p-1, n-1):
            print("le joueur 1 a gagné")
            print("la nouvelle table :")
            print(tab)
            ecrire(tab)
        else:
            print("le joueur 2 a gagné")
    else:
        if (x2,y2) == (0,0) or (x1,y1) == (0,0):
            print("le joueur 2 a gagné")
        else:
            print("le joueur 1 a gagné")
            print("la nouvelle table :")
            print(tab)
            ecrire(tab)
                
#partie_learning(8,6)
                
            
#____________________________________________ VERS UN APPRENTISSAGE EFFICACE

liste_coups_possibles = ["H", "B", "G", "D","H", "B", "G", "D","H", "B", "G", "D", "HG", "HD", "BG", "BD"]
taille_gen = 40


def plan_de_jeu_aleatoire(taille_gen):
    """ Fonction qui construit aléatoirement (selon une certaine loi fixée) un plan_de_jeu
(c'est-à-dire une suite de coups à jouer)
taille_gen est la taille du plan_de_jeu à construire (c'est-à-dire le nombre maximum de tours joués).
"""
    res = []
    for i in range(taille_gen):
        p_i = random.randint(0,12)
        if p_i == 12:
            res.append("DET")
        else:
            res.append(liste_coups_possibles[p_i])
        if p_i == 12:
            p_i_2 = random.randint(0,1)
            if p_i_2 == 0:
                res.append("DET")
            else:
                x_i = random.randint(0,n-1)
                y_i = random.randint(0,p-1)
                while (x_i,y_i) == (0,0) or (x_i,y_i) == (n-1,p-1):
                    x_i = random.randint(0,n-1)
                    y_i = random.randint(0,p-1)
                res.append([x_i,y_i])
        else :
            x_i = random.randint(0,n-1)
            y_i = random.randint(0,p-1)
            while (x_i,y_i) == (0,0) or (x_i,y_i) == (n-1,p-1):
                x_i = random.randint(0,n-1)
                y_i = random.randint(0,p-1)
            res.append([x_i,y_i])
    return res

def distance(x,y,terrain,obj = 0):
    """ Fonction distance qui permet de calculer la distance
d'une case à un camp (camp donné par l'objectif 'obj' )
"""
    if obj == 0:
        if (x,y) == (0,0):
            return 0
        elif isinstance(terrain[x][y], int):
            return terrain[x][y] + min(distance(x-1,y,terrain,obj),distance(x,y-1,terrain,obj))
        else:
            return 100000
    else:
        if (x,y) == (n-1,p-1):
            return 0
        elif isinstance(terrain[x][y], int):
            return terrain[x][y] + min(distance(x+1,y,terrain,obj),distance(x,y+1,terrain,obj))
        else:
            return 100000

def detruire_bot(x,y,terrain,m,mom,marq):
    """ Fonction permettant d'appeler les bonnes fonctions de suppression"""
    deli = 0
    if x-1 >= 0 and isinstance(terrain[x-1][y],int) and terrain[x-1][y] > 0:
        (x,y,mom,deli) = del_h(x,y,terrain)
    elif y-1 >= 0 and isinstance(terrain[x][y-1],int) and terrain[x][y-1] > 0:
        (x,y,mom,deli) = del_g(x,y,terrain)
    elif x+1 <= n-1 and isinstance(terrain[x+1][y],int) and terrain[x+1][y] > 0:
        (x,y,mom,deli) = del_b(x,y,terrain)
    elif y+1 <= p-1 and isinstance(terrain[x][y+1],int) and terrain[x][y+1] > 0:
        (x,y,mom,deli) = del_d(x,y,terrain)
    return (x,y,mom,deli)
    

def coup_bot_dl(x,y,terrain,tour,mom,marq,deli, obj, ennemi, plan_de_jeu):
    """Fonction analogue à "joueur" ou "bot_1" mais dédiée au bot en apprentissage par sélection génétique."""
    global n
    n = len(terrain)
    global p
    p = len(terrain[0])
    tab = recup()
    tourbi = tour % 2
    tourdiv = tour // 2
    m = mom
    print(tour)
    coup = plan_de_jeu[0][tour]
    
    if tourbi == 0:
        if coup == "DET":
            return detruire_bot(x,y,terrain,m,mom,marq)
        elif coup_possible([coup],x,y,terrain,m):
            (x,y,m,mom) = filtrage(coup, x, y, terrain, m, mom, marq)
            return (x,y,mom,0)
        else:
            return bot_1(x,y,terrain,tour,mom,marq,deli,obj, ennemi = "j1")
    else:
        if coup == "DET":
            return detruire_bot(x,y,terrain,m,mom,marq)
        elif isinstance(terrain[coup[0]][coup[1]],int):
            terrain[coup[0]][coup[1]] += 1
            return (x,y,mom,deli)
        else:
            return bot_1(x,y,terrain,tour,mom,marq,deli,obj, ennemi = "j1")
        


def partie_genetique(n, p, j1, j2, plan_de_jeu, N):
    """Fonction analogue à la fonction "partie" qui permet de faire jouer
correctement les fonctions liée à l'algorithme génétique de sélection.
"""
    print("nouvelle partie")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    terrain = [[0 for i in range(n)] for j in range(p)]
    x1,y1 = 1,1
    x2,y2 = (p-2),(n-2)
    tour = 0
    premierjoueur = 0
    mom1,mom2 = 1,1
    del1,del2 = 0,0
    terrain[x1][y1] = "j1"
    terrain[x2][y2] = "j2"
    while (x1,y1) != ((p-1),(n-1)) and (x2,y2) != (0,0) and (x1,y1) != (0,0) and (x2,y2) != ((p-1),(n-1)) and tour < N:
        if premierjoueur <= 1:
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(3)
            print(Fore.YELLOW + "joueur1: ( de momentum =", mom1, ")" + Fore.BLACK)
            (x1,y1,mom1,del1) = j1(x1,y1,terrain,tour,mom1,"j1",del1,1, "j2")
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(0.7)
            print(Fore.GREEN + "joueur2: ( de momentum =", mom2, ")" + Fore.BLACK)
            (x2, y2,mom2,del2) = j2(x2,y2,terrain,tour,mom2, "j2",del2,0,"j1" ,plan_de_jeu)
            print(x2,y2,mom2,del2)
            tour = (tour+1)
            premierjoueur +=1
        else:
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(3)
            print(Fore.GREEN + "joueur2: ( de momentum =", mom2, ")" + Fore.BLACK)
            (x2, y2, mom2, del2) = j2(x2,y2,terrain,tour,mom2,"j2",del2,0,"j1", plan_de_jeu)
            print_terrain(terrain, Fore.GREEN, Fore.YELLOW)
            sleep(0.7)
            print(Fore.YELLOW + "joueur1: ( de momentum =", mom1, ")" + Fore.BLACK)
            (x1, y1, mom1, del1) = j1(x1,y1,terrain,tour,mom1, "j1",del1,1, "j2")
            tour = (tour+1)
            premierjoueur +=1
            if premierjoueur >= 4:
                premierjoueur = 0
            
    if premierjoueur <= 2:
        if (x1,y1) == (p-1,n-1) or (x2, y2) == (p-1, n-1):
            print("le joueur 1 a gagné")
            return 100000 + (N-tour)
        else:
            print("le joueur 2 a gagné")
            return tour
    elif tour <= N :
        if (x2,y2) == (0,0) or (x1,y1) == (0,0):
            print("le joueur 2 a gagné")
            return tour
        else:
            print("le joueur 1 a gagné")
            return 100000 + (N-tour)
    else:
        return distance(x,y,terrain,0) + N



def mutation(plan_de_jeu, nb_mut):
    """ Fonction qui modifie nb_mut fois le plan_de_jeu en apportant des mutations aléatoires."""
    longueur = len(plan_de_jeu)
    for i in range(nb_mut - 1):
        c_i = random.randint(0, longueur - 1)
        if c_i % 2 == 0:
            p_i = random.randint(0,12)
            if p_i == 12:
                plan_de_jeu[0][c_i] = "DET"
            else:
                plan_de_jeu[0][c_i] = liste_coups_possibles[p_i]
        else:
            if plan_de_jeu[0][c_i - 1] == "DET":
                p_i_2 = random.randint(0,1)
                if p_i_2 == 0:
                    plan_de_jeu[0][c_i] = "DET"
                else:
                    x_i = random.randint(0,n-1)
                    y_i = random.randint(0,p-1)
                    while (x_i,y_i) == (0,0) or (x_i,y_i) == (n-1,p-1):
                        x_i = random.randint(0,n-1)
                        y_i = random.randint(0,p-1)
                    plan_de_jeu[0][c_i] = [x_i,y_i]
            else:
                x_i = random.randint(0,n-1)
                y_i = random.randint(0,p-1)
                while (x_i,y_i) == (0,0) or (x_i,y_i) == (n-1,p-1):
                    x_i = random.randint(0,n-1)
                    y_i = random.randint(0,p-1)
                plan_de_jeu[0][c_i] = [x_i,y_i]
                
def calcul(lst, n, p, N):
    """ Fonction intermédiaire qui permet le calcul de l'efficacité d'une génération de plan_de_jeu"""
    res = []
    for i in range(len(lst)):
        pdj_i = lst[i]
        val = partie_genetique(n, p, bot_1, coup_bot_dl, pdj_i, N)
        res.append([pdj_i[0],val])
    return res

def selection_update(gen_i, taille_gen):
    """ Fonction de sélection génétique de l'algorithme de sélection génétique."""
    long = len(gen_i)
    nb_copie = long // 5
    for i in range(1,nb_copie):
        for j in range(5):
            temp = copy.deepcopy(gen_i[j])
            mutation(temp, (i*nb_copie + j))
            gen_i[i*nb_copie + j] = temp
    gen_i[long - 1] = [plan_de_jeu_aleatoire(taille_gen),0]
    

def algorithme_de_selection(nb_gen, nb_par_gen, nb_tour, n, p):
    """ Fonction à la tête de l'algorithme de sélection génétique."""
    gen_0 = []
    for i in range(nb_par_gen):
        gen_0.append([plan_de_jeu_aleatoire(nb_tour), 0])
    gen_i = gen_0
    for i in range(nb_gen):
        print("algo de sel tour :")
        print(i)
        print(gen_i)
        gen_i = calcul(gen_i, p, n, nb_tour)
        print("après calcul numéro :")
        print(i)
        print(gen_i)
        triliste(gen_i)
        print("après tri de la liste numéro :")
        print(i)
        print(gen_i)
        selection_update(gen_i, nb_tour)
        print("après selection numéro :")
        print(i)
        print(gen_i)
        sleep(0.1)
        
def main():
    """ Fonction qui lance l'algorithme de sélection pour les conditions imposées dans la fonction. """
    global n
    global p
    n = 6
    p = 4
    #pdj_0 = plan_de_jeu_aleatoire(5)
    #lala = partie_genetique(7,9,bot_1,coup_bot_dl, pdj_0, 50)
    #mutation(pdj_0,1)
    algorithme_de_selection(50,25,30, n,p)
    return None

def illustration_1():
    """ Fonction permettant de lancer une partie d'un joueur contre un autre."""
    partie(4,6,joueur,joueur)
    
def illustration_2():
    """ Fonction permettant de lancer une partie d'un joueur contre un bot naïf."""
    partie(4,6,joueur,bot_1)
    
def illustration_3():
    """ Fonction permettant de lancer une partie d'un joueur contre le premier bot
en apprentissage (bot jouant le coup le plus populaire à chaque tour)
"""
    partie_learning(4,6)

def illustration_4():
    """ Fonction montrant le jeu du bot en apprentissage par sélection génétique
ayant appris à gagner contre bot_1 (bot naïf) via l'algorithme de sélection.
le "j1" est le bot naïf.
le "j2" est le bot ayant appris.
"""
    pdj_en_7_pour_4_6 = [['G', [0, 3], 'G', [3, 3], 'H', [4, 2], 'G', [0, 2], 'G', [1, 2], 'H', [5, 0], 'H', [1, 2], 'D', [1, 2], 'H', [2, 3], 'D', [2, 1], 'D', [0, 2], 'H', [3, 3], 'D', [4, 3], 'G', [5, 2], 'G', [3, 0], 'H', [4, 2], 'H', [0, 3], 'D', [3, 0], 'D', [3, 0], 'H', [5, 0], 'H', [1, 3], 'H', [2, 1], 'D', [4, 0], 'D', [3, 3], 'B', [3, 2], 'H', [3, 3], 'D', [3, 1], 'D', [5, 1], 'DET', [4, 0], 'B', [5, 0]], 7]
    partie_genetique(4, 6, bot_1, coup_bot_dl, pdj_en_7_pour_4_6, 30)


