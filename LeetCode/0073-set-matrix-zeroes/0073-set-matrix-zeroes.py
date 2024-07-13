class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        nRow=len(matrix)
        nCol=len(matrix[0])
        
        excludeRow=set()
        excludeCol=set()
        
        for row in range(nRow):
            for col in range(nCol):
                if matrix[row][col]==0:
                    excludeRow.add(row)
                    excludeCol.add(col)
                
        for row in excludeRow:
            matrix[row]=[0 for _ in range(nCol)]
        
        for col in excludeCol:
            for row in range(nRow):
                matrix[row][col]=0
        