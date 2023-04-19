'''
TASK 2 - 1(Edited Part)
'''

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
        # so we print the first answer found in the previous step *ref) ln 127
        if explain:
            print(f"Put {grid[x][y]} in location ({x+1}, {y+1})")
        next_x,next_y=get_next(grid,x,y,n_rows,n_cols)
        solve_sudoku(grid, next_x, next_y, n_rows, n_cols, explain)
        print(grid)
        return grid

#A function that takes parameters (inputs), converts them to integers, and returns a list
def convert_inputs_to_integers(values_to_check):
	'''
	Convert inputs received from the command line (as strings) to integers
	Exits with an error message if non integer numbers are provided as inputs
	'''

	numbers_to_process = []
	for val in values_to_check:
		if val.isdigit():
			numbers_to_process.append(int(val))
		else:
			print ("Error: expected integer argument, got %s" % val)
			exit()

	return numbers_to_process

#Function that interpret input parameter from console 
def parse_command_line_arguments(argv):
    MAX_FLAGS = 8
    N_flags = 0
    explain = False

    args = input('Type in arguments: ')

     #콘솔 매개 변수로 explain이 들어왔는지 검사
    if args.__contains__('explain'):
        N_flags = N_flags + 1
        explain = True

    #(이전 버전에서 변경했음)우선 여긴 꺼둠
    #if N_flags == 0:
    #    explain = True

    #values_to_check = args[N_flags:]
    #numbers_to_process = convert_inputs_to_integers(values_to_check) #매개 변수들을 정수의 형태로 변환 및 저장
    return (explain)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''

#args -> Input entered through the console, i.e. parameters
def main():
    explain = parse_command_line_arguments() #receiving parameters
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


if __name__ == "__main__":
    main()