class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle by modifying the board in-place.
        """
        
        DIGITS = set("123456789")
        
        def box_index(i, j):
            return (i // 3) * 3 + (j // 3)
        
        # Initialize cell groups
        def initialize_groups(board):
            class Cell:
                def __init__(self, value):
                    self.value = value
                    self.possible_digits = DIGITS if value == '.' else set()

            rows = [[] for _ in range(9)]
            cols = [[] for _ in range(9)]
            boxes = [[] for _ in range(9)]

            for i in range(9):
                for j in range(9):
                    cell = Cell(board[i][j])
                    k = box_index(i, j)
                    rows[i].append(cell)
                    cols[j].append(cell)
                    boxes[k].append(cell)
                
            return rows, cols, boxes
        
        # Update possible digits for a cell
        def update_possible_digits():
            for i in range(9):
                for j in range(9):
                    cell = rows[i][j]
                    if cell.value == '.':
                        k = box_index(i, j)
                        cell.possible_digits = DIGITS \
                        - used_digits(rows[i]) \
                        - used_digits(cols[j]) \
                        - used_digits(boxes[k])

        # Get the used digits in a group
        def used_digits(group):
            return {cell.value for cell in group if cell.value != '.'}
        
        # Find the cell with the fewest possible digits
        def find_most_constrained_cell():
            min_options = 10  # More than the maximum possible options (9)
            target_cell = None
            for i in range(9):
                for j in range(9):
                    cell = rows[i][j]
                    if cell.value == '.' and len(cell.possible_digits) < min_options:
                        min_options = len(cell.possible_digits)
                        target_cell = (i, j)
            return target_cell
        
        # dfs to solve the Sudoku
        def dfs_sudoku():
            cell_pos = find_most_constrained_cell()
            if not cell_pos:
                return True  # No cells left to fill, puzzle solved
            
            i, j = cell_pos
            cell = rows[i][j]
            
            for digit in cell.possible_digits:
                cell.value = digit
                update_possible_digits()
                if dfs_sudoku():
                    return True
                cell.value = '.'
                update_possible_digits()
            
            return False
        
        rows, cols, boxes = initialize_groups(board)
        update_possible_digits()
        
        dfs_sudoku()
        
        for i in range(9):
            for j in range(9):
                board[i][j] = rows[i][j].value
