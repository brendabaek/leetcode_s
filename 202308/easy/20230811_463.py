## https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        stt = 0
        while stt < len(grid) :
            if grid[stt].count(1) == 0 : stt += 1
            else : break
        if stt != 0 : grid = grid[stt:]
        elif stt == len(grid) : return 0

        ln1, ln2, ans = len(grid), len(grid[0]), 0
        if ln1 == 1 :
            if grid[0].count(1) == 0 : return 0
            else : return (grid[0].count(1) * 2) + 2      ## grid[0].count(1) > 0

        for i in range(ln1) :
            if i == 0 :
                ans += grid[i].count(1)
                if ln2 == 1 and grid[i][0] == 1 : ans += 2
                for j in range(ln2-1) :
                    if j == 0 and grid[i][j] == 1 : ans += 1
                    if grid[i][j] == 0 and grid[i][j+1] == 1 : ans += 1
                    elif grid[i][j] == 1 and grid[i][j+1] == 0 : ans += 1
                    if j == ln2-2 and grid[i][j+1] == 1 : ans += 1

            else : # i > 0
                for j in range(ln2) :
                    if grid[i-1][j] == 0 and grid[i][j] == 1 : ans += 1
                    elif grid[i-1][j] == 1 and grid[i][j] == 0 : ans += 1
                if ln2 == 1 and grid[i][0] == 1 : ans += 2
                for j in range(ln2-1) :
                    if j == 0 and grid[i][j] == 1 : ans += 1
                    if grid[i][j] == 0 and grid[i][j+1] == 1 : ans += 1
                    elif grid[i][j] == 1 and grid[i][j+1] == 0 : ans += 1
                    if j == ln2-2 and grid[i][j+1] == 1 : ans += 1
            
            if grid[i].count(0) == ln2 : return ans
            elif i == (ln1-1) : return ans + grid[i].count(1)
        return ans