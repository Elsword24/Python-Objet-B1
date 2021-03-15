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
    taille = 0
    taille = int(input('Quelle est la taille du plateau ?'))
    Htaille = taille
    plateau = [] 
    for x in range(taille):
	    plateau.append([" "] * taille) 

    plateau[3][3] = "X" 
    plateau[3][4] = "O"
    plateau[4][3] = "O"
    plateau[4][4] = "X"
    plateau_affichage(plateau,taille,plateau_list,Htaille)
    plateau_list(taille,Htaille)

jeu()