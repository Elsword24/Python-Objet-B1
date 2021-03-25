def plateau_affichage (taille) : #def de la fonction affichage plateau
    tab = []
    print ('  ', end=' ')
    for i in range (taille+1) : #création longueur plateau
        print (i, end='  ')
        tab.append([])
    for k in range (taille+1) : #création hauteur plateau
        tab[0].append(str(i))
        print ('')
        print (k, end='  ')
        for j in range (taille+1) : # création position pion de base
            if k==4 and j== 4 :
                print ('X',end='  ')
            elif k==4 and j==5:
                print ('O',end='  ')
            elif k==5 and j==4:
                print ('O',end='  ')
            elif k==5 and j==5 :
                print ('X',end='  ')
            else :
                print ('.', end='  ') 
    tab[0][0] = " " # on remplace la case en haut à gauche par un espace
    return tab

def pose(x,tableauPions):
    #while plateaunotfull == True : #les joueurs jouent tant que le plateau n'est pas plein
        if x==1 :
            print ('Jouer un pion X')
            j=int(input('Quel colonne ?'))
            k=int(input('Quel ligne ? '))
            tab[j][k] ='X'
            x=x-1
        else :
            print ('Jouer un pion O')
            x=x+1

def jeu () : #création d'une variable pour lancer le jeu

    taille=int(input('Tailleduplateau'))  # création d'unevaraible longueur et hauteur pour le plateau
    x=1 #création variable joueur
    if taille<=5 :
        print ('Le plateau est trop petit')
    else:
        plateau_affichage(taille)
    tableauPions = plateau_affichage(taille)
    pose(x,tableauPions)

jeu()