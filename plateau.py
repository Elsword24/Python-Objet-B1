def display_checkerboard(x = int , checkerboard = []):
    for k in range(x):
            if k >= 9: 
                print(" ", end="")
            else: 
                print("  ",end="")
            print(k+1, end="")
    print("")

    for ligne in range(x):
        print(ligne + 1, end =" ")
        for colone in range(x):
                if ligne < 9 and colone == 0:
                    print(" ", end = "")
                elif ligne >= 9 :
                    print('',end = "") 
                print(checkerboard[ligne][colone], end = "  ")
        print("")

def checkerboard_list(x = int, y = int ):
    damier = x  * ['.']
    for i in range(len(damier)):
        damier[i] = y * ['.']
    return damier

display_checkerboard()