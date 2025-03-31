#maze with River

def maze_with_river(p,r,c):

    if r == 1 and c==1 :
        print(p)

    if r == 2 and c ==2 :
        return 
    if r > 1 :

        down = maze_with_river(p+'D',r-1,c)

    if c > 1 :
        right = maze_with_river(p+'R',r,c-1)

    if r>1 and c>1 :
        diagonal = maze_with_river(p+'V',r-1,c-1)

maze_with_river("",3,3)



    