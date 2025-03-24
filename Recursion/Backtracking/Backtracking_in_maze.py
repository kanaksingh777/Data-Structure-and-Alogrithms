def backtrack_maze(p,maze,r,c):

    if r == len(maze)-1 and c== len(maze[0])-1 :

        print(p)
        return
    if (not maze[r][c]):
        return 
    maze[r][c] = False

    if r < len(maze)-1:

        down = backtrack_maze(p+"D",maze,r+1,c)


    if c <len(maze[0])-1:
        right = backtrack_maze(p + "R",maze,r,c+1)

    if r >0 :
        up = backtrack_maze(p + "U",maze,r-1,c)

    if  c >0 :
        left = backtrack_maze(p + "L",maze,r,c-1)

    maze[r][c] = True
    
maze =[[True,True,True],
       [True,True,True],
       [True,True,True]]

backtrack_maze("",maze,0,0)