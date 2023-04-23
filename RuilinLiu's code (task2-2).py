#!/usr/bin/env python3
import copy
import time

###################################################### Task 2-2's libraries
import os    #This library is for open file
from os.path import dirname, abspath    #This library is for get the file path
import re    #This library is for extract numbers from a string
######################################################


########################################################################### Change there for Task2-2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
grid1=[]


###########################################################################

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
    box=[grid[i*n_rows+r][j*n_cols+c] for r in range(n_rows) for c in range(n_cols)]
    v=set([x for x in range(1,n+1)])-set(box)-set(grid[x])-set(list(zip(*grid))[y])
    return list(v)

def solve_sudoku(grid,x,y,n_rows,n_cols):
    for grid[x][y] in value(grid,x,y,n_rows,n_cols):
        next_x,next_y=get_next(grid,x,y,n_rows,n_cols)
        if next_y==-1:
            return True
        elif solve_sudoku(grid,next_x,next_y,n_rows,n_cols):
            return True
        else:
            grid[x][y]=0


def solve(grid,n_rows,n_cols):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''
    x, y = star_pos(grid,n_rows,n_cols)
    solve_sudoku(grid, x, y,n_rows,n_cols)
    print(grid)
    return grid


#####################################Task2-2####################################################
def read_file(filename):    #By Ruilin Liu
    '''
    This function is used to read a file, and put them into a list to
    set up a new grid.
    '''
    global in_filename
    in_filename = filename    #Use for function "output"

    current_path = abspath(dirname(__file__))    #Get the current path
    file_path = os.path.join(current_path,'grids\\',filename)  #This is the path of the file

    with open(file_path,'r') as f:  #Open the file
        lines=f.readlines()    #Read all lines in the file

        for line in lines:
            number = re.findall("\d+",line)  #Extract numbers from each line
            l=[]
            for i in number:
                l.append(int(i))
            grid1.append(l)    #Append the list into grid2 as a sub-list
    f.close()

read_file('med2')    #!!!!!!!!!!!This will be changed by the flag!!!!!!!!!!!!
                     #Must enter the fullname of the file!!!!!!!!!!!!!!!!!!!!


def find_grid_size(grid):
    '''
    This function is used to find the size of grid.
    '''
    global grid_row, grid_column, grids

    if len(grid) == 4 and len(grid[0]) == 4:  #2*2 grid
        grid_row = 2
        grid_column = 2
    elif len(grid) == 6 and len(grid[0]) == 6:  #2*3 grid
        grid_row = 2
        grid_column = 3
    elif len(grid) == 9 and len(grid[0]) == 9:  #3*3 grid
        grid_row = 3
        grid_column = 3

    grids = [[grid1, grid_row, grid_column]]  #This is moved from the beginning of the solver
                                              #Which tell solver which grid need be solved and the,
                                              #size of the grid

find_grid_size(grid1)


def output(out_grid, explain):
    '''
    This function is output the finall solution into 
    '''

    out_filename = "Output_of_'" + in_filename + "'.txt" #Combine old file name and 'Output of'


    current_path = abspath(dirname(__file__))    #Get the current path
    file_path = os.path.join(current_path,'output\\',out_filename)  #This is the path of the output file
    
    f = open(file_path, 'w')
    f.write("The correct solution of file ''"+ in_filename + "'' is:\n\n")

    for line in out_grid:
        for i in line:    
            f.write(str(i) + ', ')
        f.write('\n')
    f.close






#####################################Task2-2####################################################


def main():
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = solve(grid,n_rows,n_cols)
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
    
    
    output(solution, 0)    #############################################Change for Task2-2

if __name__ == "__main__":
    main()