# 840. Magic Squares In Grid
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are
# there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may 
# contain numbers up to 15.

class Solution:
    def isMagicSquare(self, grid, r, c):
        s = grid[r][c] + grid[r][c+1] + grid[r][c+2]
        seen = set()

        for i in range(3):
            for j in range(3):
                num = grid[r+i][c+j]
                if num < 1 or num > 9 or num in seen:
                    return False
                seen.add(num)

        for i in range(3):
            if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != s:
                return False
            if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != s:
                return False

        if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
            return False
        if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
            return False

        return True

    def numMagicSquaresInside(self, grid):
        m, n = len(grid), len(grid[0])
        cnt = 0

        for i in range(m - 2):
            for j in range(n - 2):
                if self.isMagicSquare(grid, i, j):
                    cnt += 1
        return cnt