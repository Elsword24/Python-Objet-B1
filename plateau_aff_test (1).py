def plateau_affichage(plateau,taille,plateau_list,Htaille,plateau_lists = []) :
    L=taille
    H=taille
    for x in range (0,L+1) :
         print (str(x),(' '), end='') 
    for y in range (0,H+1) :
        if y==0 :
            print (' ')
        else :
            print (str(y), )
        for y in range(H):
            if x < 8 and y == 0:
                print(" ", end = "")
            elif x >= 8 :
                print('',end = "") 
            print(plateau_lists[taille][Htaille], end = "  ")
        print("")
            
        

def plateau_list(taille,Htaille):
    damier = taille  * ['.']
    for i in range(len(damier)):
        damier[i] = Htaille * ['.']
    return damier

def jeu() :
    taille = int(input('Quelle est la taille du plateau ?'))

    taillePlateau: int = taille + 1

    plateau = [['.']*taillePlateau] * taillePlateau
    plateau[0] = list(range(1, taillePlateau))
        
    #plateau[taille/2 - 1][taille/2 - 1] = plateau[taille/2][taille/2] = 'x'
    #plateau[taille/2 - 1][taille/2] = plateau[taille/2][taille/2 - 1] = 'o'

    #for x in range(taille + 1):
    #    if x == 0:
    #        print(' ')
    #    else: 
    #        print(x)

    for i in range(len(plateau)):
        plateau[i][0] = i

    for row in plateau:
        print(*row)

    print(plateau)
    #plateau_affichage(plateau,taille,plateau_list,Htaille)
    #plateau_list(taille,Htaille)

jeu()