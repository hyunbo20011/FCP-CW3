#!/usr/bin/env python3
import copy
import time
import matplotlib.pyplot as plt
import numpy
import sys  #
import os  # This library is for open file
from os.path import dirname, abspath  # This library is for get the file path
import re  # This library is for extract numbers from a string

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

easy1 = [
    [9, 0, 6, 0, 0, 1, 0, 4, 0],
    [7, 0, 1, 2, 9, 0, 0, 6, 0],
    [4, 0, 2, 8, 0, 6, 3, 0, 0],
    [0, 0, 0, 0, 2, 0, 9, 8, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 9, 4, 0, 8, 0, 0, 0, 0],
    [0, 0, 3, 7, 0, 8, 4, 0, 9],
    [0, 4, 0, 0, 1, 3, 7, 0, 6],
    [0, 6, 0, 9, 0, 0, 1, 0, 8]]

easy2 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]

easy3 = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 5, 6, 0, 3],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 3, 0, 5],
    [0, 6, 4, 0, 3, 1],
    [0, 0, 1, 0, 4, 6]]

med1 = [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 1],
    [3, 6, 9, 0, 8, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 6, 8, 0, 0],
    [0, 0, 0, 1, 3, 0, 0, 0, 9],
    [4, 0, 5, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 6, 0, 0, 7, 0, 0, 0],
    [1, 0, 0, 3, 4, 0, 0, 0, 0]]

med2 = [
    [8, 0, 9, 0, 2, 0, 3, 0, 0],
    [0, 3, 7, 0, 6, 0, 5, 0, 0],
    [0, 0, 0, 4, 0, 9, 7, 0, 0],
    [0, 0, 2, 9, 0, 1, 0, 6, 0],
    [1, 0, 0, 3, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 3],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [5, 0, 0, 0, 0, 0, 0, 1, 4],
    [0, 0, 0, 2, 8, 4, 6, 0, 5]]

hard1 = [
    [0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3)]
#grids1 = [(easy1, 3, 3),(easy2, 3, 3), (easy3, 2, 3), (med1, 3, 3), (med2, 3, 3), (hard1, 3, 3)]


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


def star_pos(grid, n_rows, n_cols):
    n = n_rows * n_cols
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                return x, y


def get_next(grid, x, y, n_rows, n_cols):
    n = n_rows * n_cols
    for next_y in range(y + 1, n):
        if grid[x][next_y] == 0:
            return x, next_y
    for next_x in range(x + 1, n):
        for next_y in range(0, n):
            if grid[next_x][next_y] == 0:
                return next_x, next_y
    return -1, -1


def value(grid, x, y, n_rows, n_cols):
    n = n_rows * n_cols
    i, j = x // n_rows, y // n_cols
    box = [grid[i * n_rows + r][j * n_cols + c] for r in range(n_rows) for c in range(n_cols)]
    v = set([x for x in range(1, n + 1)]) - set(box) - set(grid[x]) - set(list(zip(*grid))[y])
    return list(v)


def solve_sudoku(grid, x, y, n_rows, n_cols):
    for grid[x][y] in value(grid, x, y, n_rows, n_cols):
        next_x, next_y = get_next(grid, x, y, n_rows, n_cols)
        if next_y == -1:
            return True
        elif solve_sudoku(grid, next_x, next_y, n_rows, n_cols):
            return True
        else:
            grid[x][y] = 0


zero_position = []  # This list contain all 0 position for each grid in each sub-list, it's add from function "explain"
all_grid_explain = []  # This list contain explanations for all grids


# origin_grid=original grid shown at the beginning, grid = Solved(Filled the grid instead of 0, xlen=Length of Row, ylen=Length of column )
def explain(origin_grid, grid, xlen, ylen):  # Write explain function to make a flag
    '''
    The reason I use for loop twice is to find a right answer by using all the numbers
    If loop is to find a 0 from the origin grid
    '''
    zero_position_list = []  # This list is use for add sub-list into zero_position for each grid
    explanation = []  # This list is use for contain explanation sentence for each grid

    for x in range(1, xlen + 1):  # Set a range from 0 to end of the row
        for y in range(1, ylen + 1):  # set a range from 0 to end of the column
            if (origin_grid[x - 1][y - 1] == 0):  # Find an empty grid from the original and output the right answer

                explain_sentance = f"put {grid[x - 1][y - 1]} in ({x}, {y})"
                print(explain_sentance)

                zero_position_list.append((x, y))
                explanation.append(explain_sentance)

    zero_position.append(zero_position_list)  # Add all sub-list to zero_position
    all_grid_explain.append(explanation)  # Add all sub-list to all_grid_explain


def solve(grid, n_rows, n_cols, show_explain):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''

    full_row = len(grid)  # full_row = Full length of the row
    full_col = len(grid[0])  # fill_col = Full length of the column
    origin_grid = [[grid[i][j] for j in range(full_col)] for i in
                   range(full_row)]  # Paste all the numbers in original grid

    x, y = star_pos(grid, n_rows, n_cols)
    solve_sudoku(grid, x, y, n_rows, n_cols)
    print(grid)

    if (show_explain):
        explain(origin_grid, grid, full_row, full_col)  # To make a explain flag
    origin_grid.clear()

    return grid


def read_file(filename):  # Task2-2
    '''
    This function is used to read a file, and put them into a list to
    set up a new grid.
    '''
    global in_filename, in_grid
    in_filename = filename  # Use for function "output"

    in_grid = []

    current_path = abspath(dirname(__file__))  # Get the current path
    file_path = os.path.join(current_path, 'grids\\', filename)  # This is the path of the file

    with open(file_path, 'r') as f:  # Open the file
        lines = f.readlines()  # Read all lines in the file

        for line in lines:
            number = re.findall("\d+", line)  # Extract numbers from each line
            l = []
            for i in number:
                l.append(int(i))
            in_grid.append(l)  # Append the list into grid2 as a sub-list
    f.close()


def find_grid_size(grid):  # Task2-2
    '''
    This function is used to find the size of grid.
    '''
    global grid_row, grid_column, grids

    if len(grid) == 4 and len(grid[0]) == 4:  # 2*2 grid
        grid_row = 2
        grid_column = 2
    elif len(grid) == 6 and len(grid[0]) == 6:  # 2*3 grid
        grid_row = 2
        grid_column = 3
    elif len(grid) == 9 and len(grid[0]) == 9:  # 3*3 grid
        grid_row = 3
        grid_column = 3

    grids = [[grid, grid_row, grid_column]]  # This is moved from the beginning of the solver
    # Which tell solver which grid need be solved and the,
    # size of the grid


def output(out_grid, explain):  # Task2-2
    '''
    This function is output the finall solution into
    '''
    out_filename = "Output_for_'" + in_filename + "'.txt"  # Combine old file name and 'Output of'

    current_path = abspath(dirname(__file__))  # Get the current path
    file_path = os.path.join(current_path, 'output\\', out_filename)  # This is the path of the output file

    f = open(file_path, 'w')  # Output the correct grid
    f.write("The correct solution of file ''" + in_filename + "'' is:\n\n")

    for line in out_grid:
        for i in line:
            f.write(str(i) + ', ')  # Outputnumber and ","
        f.write('\n')

    if explain == 0:  # Output explaination if explain not equal 0
        return 0
    else:
        f.write("\n\n\nExplanation of how to fill correct number in the file ''" + in_filename + "'' is:\n\n")
        for line in explain:
            for i in line:
                f.write(i)
                f.write('\n')

    f.close

def plot(time,time1,time2):
    if len(time)==0 and len(time1)==0:
        timeaverage = {'2*2 grid': sum(time) ,
                       '2*3 grid': sum(time1) ,
                       '3*3 grid': sum(time2) / len(time2)}
        plt.bar(timeaverage.keys(), timeaverage.values(), color=['yellow', 'green', 'blue'])
        plt.xlabel('size')
        plt.ylabel('time(s)')
        plt.title('Average solving time for different size grid')
        plt.show()
    elif len(time)==0 and len(time2)==0:
        timeaverage = {'2*2 grid': sum(time),
                       '2*3 grid': sum(time1) / len(time1),
                       '3*3 grid': sum(time2)}
        plt.bar(timeaverage.keys(), timeaverage.values(), color=['yellow', 'green', 'blue'])
        plt.xlabel('size')
        plt.ylabel('time(s)')
        plt.title('Average solving time for different size grid')
        plt.show()
    elif len(time1)==0 and len(time2)==0:
        timeaverage = {'2*2 grid': sum(time)/len(time),
                       '2*3 grid': sum(time1) ,
                       '3*3 grid': sum(time2)}
        plt.bar(timeaverage.keys(), timeaverage.values(), color=['yellow', 'green', 'blue'])
        plt.xlabel('size')
        plt.ylabel('time(s)')
        plt.title('Average solving time for different size grid')
        plt.show()
    elif len(time)==0:
        timeaverage = {'2*2 grid': sum(time),
                       '2*3 grid': sum(time1) / len(time1),
                       '3*3 grid': sum(time2)/len(time2)}
        plt.bar(timeaverage.keys(), timeaverage.values(), color=['yellow', 'green', 'blue'])
        plt.xlabel('size')
        plt.ylabel('time(s)')
        plt.title('Average solving time for different size grid')
        plt.show()
    elif len(time1)==0:
        timeaverage = {'2*2 grid': sum(time)/len(time),
                       '2*3 grid': sum(time1),
                       '3*3 grid': sum(time2) / len(time2)}
        plt.bar(timeaverage.keys(), timeaverage.values(), color=['yellow', 'green', 'blue'])
        plt.xlabel('size')
        plt.ylabel('time(s)')
        plt.title('Average solving time for different size grid')
        plt.show()
    elif len(time2)==0:
        timeaverage = {'2*2 grid': sum(time) / len(time),
                       '2*3 grid': sum(time1) / len(time1),
                       '3*3 grid': sum(time2)}
        plt.bar(timeaverage.keys(), timeaverage.values(), color=['yellow', 'green', 'blue'])
        plt.xlabel('size')
        plt.ylabel('time(s)')
        plt.title('Average solving time for different size grid')
        plt.show()

MAX_FLAGS = 4


def parse_command_line_arguments(argv, if_out):
    '''
    Function that interpret input parameter from console
    first variable is all arguemnts, Second is for output file, because there's a logical error
    '''
    global show_explain
    global TIme,Time1,Time2

    show_explain = False
    show_file = False

    ######################Flag --profile#########################
    if '--profile' in argv[0:MAX_FLAGS]:
        plot(Time2, Time1, Time)

    ######################Flag --Explain#########################
    # To check if 'explain' was passed as a console parameter
    if '--explain' in argv[0:MAX_FLAGS]:
        show_explain = True

    ######################Flag --file#########################
    if '--file' in argv[0:MAX_FLAGS] and if_out == 0:
        show_file = True
        try:
            file_name_location = 0
            for i in argv:  # Find the file's name
                if i == '--file':
                    break
                else:
                    file_name_location = file_name_location + 1
            file_name = argv[file_name_location + 1]

            read_file(file_name)
            find_grid_size(in_grid)

        except:
            try:
                os.system('cls')  # Remove all print in the terminal on Windows
            except:
                os.system('clear')  # Remove all print in the terminal on Linux or Mac
            print("Please enter right fullname of file include extension and try it again!!!")
            print("And please leave a space between '--file' and filename.")
            sys.exit()  # If file name is wrong, exit the program and print error message

    elif '--file' in argv[0:MAX_FLAGS] and if_out == 1:
        if show_explain == False:
            output(solution, 0)  # For Task2-2 file output
        elif show_explain == True:
            output(solution, all_grid_explain)


    ######################  Add flags below this line  #########################

    return (show_explain)  # Return this value to main funcion


def main(args):
    global solution

    points = 0
    show_explain = parse_command_line_arguments(args, 0)  # receiving parameters, first variable is all arguemnts
    # Second is for output file, because there's a logical error

    print("Running test script for coursework 1")
    print("====================================")

    Time = []
    Time1 = []
    Time2 = []

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols, show_explain)
        elapsed_time = time.time() - start_time
        if n_rows==3 and n_cols==3:
            Time.append(elapsed_time)
        elif n_rows==2 and n_cols==3:
            Time1.append(elapsed_time)
        elif n_rows==2 and n_cols==2:
            Time2.append(elapsed_time)
        print("Solved in: %f seconds" % elapsed_time)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    #plot(Time2,Time1,Time)

    print("====================================")
    print("Test script complete, Total points: %d" % points)

    parse_command_line_arguments(args, 1)  # receiving parameters, first variable is all arguemnts
    # Second is for output file, because there's a logical error


if __name__ == "__main__":
    main(sys.argv[1:])  # To get flags