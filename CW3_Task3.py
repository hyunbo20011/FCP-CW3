def solve_sudoku(board):
    # Create a set to store the possible values for each empty cell
    possible_values = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possible_values[(i, j)] = set(range(1, 10))

    # Create a queue for wavefront solver
    queue = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                queue.append((i, j))

    # Solve the puzzle using wavefront solver
    while queue:
        i, j = queue.pop(0)
        box_i, box_j = (i // 3) * 3, (j // 3) * 3
        for x in range(9):
            # Check row
            if board[i][x] != 0 and (i, x) in possible_values:
                possible_values[(i, j)].discard(board[i][x])
            # Check column
            if board[x][j] != 0 and (x, j) in possible_values:
                possible_values[(i, j)].discard(board[x][j])
            # Check box
            if board[box_i + (x // 3)][box_j + (x % 3)] != 0 and \
                    (box_i + (x // 3), box_j + (x % 3)) in possible_values:
                possible_values[(i, j)].discard(board[box_i + (x // 3)][box_j + (x % 3)])

        # If there is only one possible value for the cell, fill it in and add to the queue
        if len(possible_values[(i, j)]) == 1:
            board[i][j] = possible_values[(i, j)].pop()
            queue.append((i, j))
            del possible_values[(i, j)]

    # Check if the puzzle is solved
    if not possible_values:
        return board

    # If there are still empty cells, use recursion to fill them in
    cell = min(possible_values, key=lambda x: len(possible_values[x]))
    for value in possible_values[cell]:
        board[cell[0]][cell[1]] = value
        solution = solve_sudoku(board)
        if solution is not None:
            return solution
        board[cell[0]][cell[1]] = 0

    return None
