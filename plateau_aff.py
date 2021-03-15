def plateau_affichage() :
    L=int(input('Longueur du plateau:'))
    H=int(input('hauteur du plateau'))
    for x in range (0,L) :
         print (str(x),(' '), end='') 
    for y in range (0,H) :
        if y==0 :
            print ('',)
        else :
            print (str(y))
    for x in range(L):
        print(x + 1, end =" ")
    for y in range(L):
            if x < 9 and y == 0:
                    print(" ", end = "")
            elif x >= 9 :
                print('',end = "") 
            print(plateau[x][y], end = "  ")
    print("")

def plateau_list(x = int, y = int ):
    damier = x  * ['.']
    for i in range(len(damier)):
        damier[i] = y * ['.']
    return damier

def jeu() :
    plateau = [] 
    for x in range(size):
	    plateau.append([" "] * size) 

    plateau[3][3] = "X" 
    plateau[3][4] = "O"
    plateau[4][3] = "O"
    plateau[4][4] = "X"
    plateau_affichage()

jeu()