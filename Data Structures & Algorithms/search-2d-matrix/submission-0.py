class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for k in matrix:
            if target in k:
                return True
        return False
        
        