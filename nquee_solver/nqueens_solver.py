class NQueensSolver:
    def __init__(self, N):
        self.N = N
        self.solutions = []

    def solve(self):
        self.solutions = []
        board = [-1] * self.N
        self._place_queen(0, board)
        return self.solutions

    def _place_queen(self, row, board):
        if len(self.solutions) >= 100:  # Stop after 100 solutions
            return

        if row == self.N:
            self.solutions.append(board.copy())
            return

        for col in range(self.N):
            if self._is_safe(row, col, board):
                board[row] = col
                self._place_queen(row + 1, board)
                board[row] = -1  # Backtrack

    def _is_safe(self, row, col, board):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True