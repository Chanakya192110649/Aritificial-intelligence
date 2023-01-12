import random

def minimax(state, depth, player):
    if player == "AI":
        best = [-1, -1, -float('inf')]
    else:
        best = [-1, -1, float('inf')]
    
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]
    
    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        if player == "AI":
            score = minimax(state, depth - 1, "Human")[2]
        else:
            score = minimax(state, depth - 1, "AI")[2]
        state[x][y] = " "
        score[0], score[1] = x, y

        if player == "AI":
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
                
    return best

def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == " ":
                cells.append([x, y])
    return cells

def game_over(state):
    # Return True if the game is over, False otherwise
    pass

def evaluate(state):
    # Evaluate the state of the game
    pass

def play(state, AI):
    while not game_over(state):
        # Human turn
        x, y = None, None
        while x is None and y is None:
            move = input("Your move (x y): ").strip().split()
            x, y = int(move[0]), int(move[1])
            if [x, y] not in empty_cells(state):
                print("Invalid move")
                x, y = None, None
        state[x][y] = "Human"
        if game_over(state):
            break
            
        # AI turn
        if AI:
            ai_move = minimax(state, depth, "AI")
            x, y = ai_move[0], ai_move[1]
            state[x][y] = "AI"
            
    print_board(state)
    if win(state, "Human"):
        print("Human wins!")
    elif win(state, "AI"):
        print("AI wins!")
    else:
        print("It's a draw!")
