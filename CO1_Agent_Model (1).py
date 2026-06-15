from dataclasses import dataclass

ROWS = 6
COLS = 7

@dataclass
class State:
    board: list

class ConnectFourProblem:
    def initial_state(self):
        return State([[0 for _ in range(COLS)] for _ in range(ROWS)])

    def actions(self, state):
        return [c for c in range(COLS) if state.board[0][c] == 0]

if __name__ == "__main__":
    problem = ConnectFourProblem()
    state = problem.initial_state()
    print("Available Actions:", problem.actions(state))
