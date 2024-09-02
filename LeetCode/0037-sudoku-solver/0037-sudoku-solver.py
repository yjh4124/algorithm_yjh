class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle by modifying the board in-place.
        """

        def box_index(i, j):
            return (i // 3) * 3 + (j // 3)

        # Initialize rows, cols, boxes to track used digits
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # Preprocess the board to fill in the used digits bitmasks
        def initialize():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        digit = int(board[i][j])
                        bit = 1 << (digit - 1)
                        rows[i] |= bit
                        cols[j] |= bit
                        boxes[box_index(i, j)] |= bit

        # Find the cell with the fewest possible digits
        def find_most_constrained_cell():
            min_options = 10
            target_cell = (-1, -1)
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    k = box_index(i, j)
                    used = rows[i] | cols[j] | boxes[k]
                    possible_digits_count = 9 - bin(used).count('1')
                    if possible_digits_count < min_options:
                        min_options = possible_digits_count
                        target_cell = (i, j)
            return target_cell

        # Backtracking DFS to solve the Sudoku
        def dfs():
            cell_pos = find_most_constrained_cell()
            if cell_pos == (-1, -1):
                return True  # No cells left to fill, puzzle solved

            i, j = cell_pos
            k = box_index(i, j)
            used = rows[i] | cols[j] | boxes[k]
            for digit in range(1, 10):
                bit = 1 << (digit - 1)
                if used & bit == 0:
                    board[i][j] = str(digit)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[k] |= bit

                    if dfs():
                        return True

                    # Revert changes if not solved
                    board[i][j] = '.'
                    rows[i] &= ~bit
                    cols[j] &= ~bit
                    boxes[k] &= ~bit

            return False

        initialize()
        dfs()
