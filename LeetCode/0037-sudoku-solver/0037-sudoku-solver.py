class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        DIGITS = set("123456789")
        
        def box_index(i, j):
            return (i // 3) * 3 + (j // 3)
        
        # Initialize cell groups
        def initialize_groups(board):
            class Cell:
                def __init__(self, value):
                    self.value=value
          
            rows=[[] for _ in range(9)]
            cols=[[] for _ in range(9)]
            boxes=[[] for _ in range(9)]

            for i in range(9):
                for j in range(9):
                    cell = Cell(board[i][j])
                    k = box_index(i, j)
                    rows[i].append(cell)
                    cols[j].append(cell)
                    boxes[k].append(cell)
                
            return rows, cols, boxes
            
        # Get the used digits in a group
        def used_digits(group):
            return set(cell.value for cell in group)
        
        # Find possible digits for a cell
        def get_possible_digits(i, j):
            k=box_index(i, j)
            digits=DIGITS\
            -used_digits(rows[i])\
            -used_digits(cols[j])\
            -used_digits(boxes[k])
            return digits
        
        # dfs to solve the Sudoku
        def dfs_sudoku():
            for i in range(9):
                for j in range(9):
                    cell=rows[i][j]
                    if cell.value!=".": continue
                    
                    for digit in get_possible_digits(i, j):
                        cell.value=digit
                        if dfs_sudoku():
                            return True
                        cell.value='.'
                    
                    return False
                
            # If no empty cell left, the board is solved
            else: 
                for row in rows:
                    print([cell.value for cell in row])
                return True
         
        
        rows, cols, boxes =initialize_groups(board)
        
        dfs_sudoku()
            
        for i in range(9):
            for j in range(9):
                board[i][j]=rows[i][j].value
        
        