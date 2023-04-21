import sys #add import sys from averages.py to use explain flag
import copy
import time

# Grids 1-5 are 2x2
grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2),(grid6, 2, 3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)

    return (squares)


def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows * n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows):
        column = []
        for row in grid:
            column.append(row[i])
        if check_section(column, n) == False:
            return False

    square = get_squares(grid, n_rows, n_cols)
    for a in square:
        if check_section(a, n) == False:
            return False
    return True

def star_pos(grid,n_rows,n_cols):
    n=n_rows*n_cols
    for x in range(n):
        for y in range(n):
            if grid[x][y]==0:
                return x,y

def get_next(grid,x,y,n_rows,n_cols):
    n=n_rows*n_cols
    for next_y in range(y+1,n):
        if grid[x][next_y]==0:
            return x,next_y
    for next_x in range(x+1,n):
        for next_y in range(0,n):
            if grid[next_x][next_y]==0:
                return next_x,next_y
    return -1,-1

def value(grid,x,y,n_rows,n_cols):
    n=n_rows*n_cols
    i,j=x//n_rows,y//n_cols
    box=[grid[i*2+r][j*2+c] for r in range(n_rows) for c in range(n_cols)]
    v=set([x for x in range(1,n+1)])-set(box)-set(grid[x])-set(list(zip(*grid))[y])
    return list(v)

def solve_sudoku(grid,x,y,n_rows,n_cols,explain): #Add explain
    for grid[x][y] in value(grid,x,y,n_rows,n_cols):
        #Find a answer for (x, y), when explain is True,
        if explain:
            print(f"Put {grid[x][y]} in location ({x+1}, {y+1})") #Print the content
        next_x,next_y=get_next(grid,x,y,n_rows,n_cols)

        if next_y==-1:
            return True
        elif solve_sudoku(grid,next_x,next_y,n_rows,n_cols,explain):
            return True
        else:
            grid[x][y]=0
        



def solve(grid,n_rows,n_cols, explain):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''
    x, y = star_pos(grid,n_rows,n_cols)
    #solve_sudoku(grid, x, y,n_rows,n_cols)
    #print(grid)

    for v in value(grid,x,y,n_rows,n_cols):
        grid[x][y]=v
        # Due to the limitation of recursive calls, the first answer found cannot be printed here, 

        next_x,next_y=get_next(grid,x,y,n_rows,n_cols)
        solve_sudoku(grid, next_x, next_y, n_rows, n_cols, explain)
        print(grid)    #Print the finall result of the grid
        return grid


MAX_FLAGS = 4  #There only 4 flags in the CW3

#Function that interpret input parameter from console 
def parse_command_line_arguments(argv):
    
    N_flags = 0
    show_explain = False

    #Check for the explain flag
    if'--explain' in argv[0:MAX_FLAGS]:
        N_flags = N_flags + 1
        show_explain = True

    
    return (show_explain)  #Return all the flag together there!!!!!!!!!!!!!!!!!!!!!!!!#


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''

#args -> Input entered through the console, i.e. parameters
def main(args):
    explain = parse_command_line_arguments(args) #receiving parameters
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = solve(grid,n_rows,n_cols,explain)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        # print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)

    '''
    Below Part is use for the flag
    '''
    
    show_explain = parse_command_line_arguments(args)




if __name__ == "__main__":
    main(sys.argv[1:])