def creerGrille(taille):
    tab = []
    for i in range(taille+1): # on crée les lignes
        tab.append([])
    for i in range(taille+1): # on modifie la première ligne
        tab[0].append(str(i))
    for i in range(1, taille+1): # on modifie les lignes suivantes
        tab[i].append(str(i)) # d'abord le chiffre
        for j in range(taille): # puis les points
            tab[i].append(".")
    tab[0][0] = " " # on remplace la case en haut à gauche par un espace
    return tab

def afficherGrille(t): #affichage du plateau
    for i in range(len(t)):
        ligne = ''
        for j in range(len(t[i])):
            ligne += " " + t[i][j]
        print(ligne)

def placerPionsCentraux(t): #placer les pions de base
    t[4][5] = 'X'
    t[4][4] = 'O'
    t[5][5] = 'O'
    t[5][4] = 'X'

def pose(x,tableauPions):
    #while plateaunotfull == True : #les joueurs jouent tant que le plateau n'est pas plein
        if x==1 : #tour du joueur 1
            print ('Jouer un pion X')
            col=int(input('Quel colonne ?'))
            lig=int(input('Quel ligne ? '))
            if tableauPions[lig][col] != '.' :
                print ("La case n'est pas vide")
            else :
                tableauPions[lig][col]= "X"
                afficherGrille(tableauPions)
        else :
            print ('Jouer un pion O')
            if tableauPions[lig][col] != '.' : #vérification de la jouabilité du coup
                print ("La case n'est pas vide")
            else :
                tableauPions[lig][col]= "O"
                afficherGrille(tableauPions) #appel de la fonction afficher grille
        print(x,lig,col) 
        verification(tableauPions,lig,col)

def retournement (tableauPions,lig,col,n,y) : #fonction retournement
    print ("Je suis entré dans retournement")
    pair=[] #création d'une liste de case a retourner
    x=1
    y=0
    if x==1 :
        symbol='X' 
        symbol2='O'
    else :
        symbol='O'
        symbol2='X'
    lig=lig-n
    col=col-y
    print (lig,col)
    print (tableauPions [lig] [col])
    while tableauPions [lig][col] !=symbol and 0<lig<9 and 0<col<9 : #On regarde autour de la pose
        print ('Je rentre dans le while')
        print (lig,col)
        if tableauPions [lig][col] ==symbol2 : #vérification du pion
            pair.append ([lig,col])
        lig=lig-n
        col=col-y
    if tableauPions [lig][col] == symbol : 
        for p in pair :
            l=p[0]
            c=p[1]
            tableauPions[l][c] = 'X'
    afficherGrille(tableauPions)

def verification (tableauPions,lig,col) :
    resultat= [] #création d'une liste contenant les directions a retourner
    x=1
    if x==1 :
        symbol='X' 
        symbol2='O'
    else :
        symbol='O'
        symbol2='X'
    tableauPions[lig][col]
    if tableauPions[lig-1][col] ==symbol2 : #au dessus
        n=1
        y=0
        resultat.append([n,y])
    if tableauPions[lig-1][col+1] == symbol2 : #en haut a droite
        n=1
        y=-1
        resultat.append([n,y])
    if tableauPions[lig][col+1] == symbol2 : #a droite
        n=0
        y=-1
        resultat.append([n,y])
    if tableauPions[lig+1][col+1] == symbol2 : #en bas a droite
        n=-1
        y=-1
        resultat.append([n,y])
    if tableauPions[lig+1][col] == symbol2 : #en bas
        n=-1
        y=0
        resultat.append([n,y])
    if tableauPions[lig+1][col-1] == symbol2 : #en bas a gauche
        n=-1
        y=1
        resultat.append([n,y])
    if tableauPions[lig][col-1] == symbol2 : #a gauche
        n=0
        y=1
        resultat.append([n,y])
    if tableauPions[lig-1][col-1] == symbol2 : #en haut a gauche
        n=1
        y=1
        resultat.append([n,y])    
    for p in resultat :
        n=p[0]
        y=p[1]
        retournement(tableauPions,lig,col,n,y)

def finjeu (tableauPions,f) :
    pionsX=[] #création de deux liste pour stocker les pions
    pionsO=[]
    for i in range (len(tableauPions)) : #défilement des cases du plateau pour vérifier si il est plein ou pas
        for j in range(len(tableauPions)) :
            if tableauPions[i][j] =="." :
                break
            if tableauPions[i][j] == 'X':
                pionsX.append([i,j])
                return (len(pionsX))
            elif tableauPions[i][j] == 'O':
                pionsO.append([i,j])
                return (len(pionsO))
            f=0 #f prends la valeur 0, fin du jeu
            return (f) #fin de la partie activé

        
def jeu ():
    f=1
    taille = 8
    tableauPions = creerGrille(taille) #création et stockage de la liste
    placerPionsCentraux(tableauPions)
    afficherGrille(tableauPions)
    while f==1 : #le jeu se poursuivra tant que f est différents de 0
        pose (1,tableauPions)
        finjeu(tableauPions,f)

jeu()