class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1 10 14
        l = 0
        r = len(matrix) - 1
        if len(matrix) == 1:
            l = 0
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        # l == 2
        l2 = 0
        r2 = len(matrix[l]) - 1
        while l2 <= r2:
            mid = (l2 + r2 + 1) // 2 # 0 + 1 + 1 // 2 -> 1
            if matrix[l][mid] == target:
                return True
            elif matrix[l][mid] < target:
                l2 = mid + 1
            else:
                r2 = mid - 1
        
        return False


