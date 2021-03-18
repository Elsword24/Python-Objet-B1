def plateau_affichage (L,H) : #def de la fonction affichage plateau
    print ('  ', end=' ')
    for i in range (1, L) : #création longueur plateau
        print (i, end='  ')
    for k in range (1,H) : #création hauteur plateau
        print ('')
        print (k, end='  ')
        for j in range (1,L) : # création position pion de base
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



def jeu () : #création d'une variable pour lancer le jeu
    L=int(input('Tailleduplateau')) +1  # création d'unevaraible longueur et hauteur pour le plateau
    H=L 
    if L-1<=5 :
        print ('Le plateau est trop petit')
    else:
        plateau_affichage(L,H)

jeu()