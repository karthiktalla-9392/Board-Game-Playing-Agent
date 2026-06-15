ROWS=6
COLS=7

board=[[0]*COLS for _ in range(ROWS)]

def valid_move(col):
    return board[0][col]==0

def explain_constraint(col):
    return "Constraint Satisfied" if valid_move(col) else "Constraint Failed: Column Full"

print(explain_constraint(3))
