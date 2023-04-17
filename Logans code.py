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


def solve_sudoku(grid,x,y,n_rows,n_cols):
    for grid[x][y] in value(grid,x,y,n_rows,n_cols):
        next_x,next_y=get_next(grid,x,y,n_rows,n_cols)
        if next_y==-1:
            return True
        elif solve_sudoku(grid,next_x,next_y,n_rows,n_cols):
            return True
        else:
            grid[x][y]=0
            
            
            
            
            '''
        
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

Function to find a zero position
'''


