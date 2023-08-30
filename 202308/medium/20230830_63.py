## https://leetcode.com/problems/unique-paths-ii/description/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1 : return 0
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[0 for j in range(c)] for i in range(r)]

        for i in range(r) :
            if obstacleGrid[i][0] == 1 : break
            else : ans[i][0] = 1
        for j in range(c) :
            if obstacleGrid[0][j] == 1 : break
            else : ans[0][j] = 1

        for i in range(1, r) :
            for j in range(1, c) :
                if obstacleGrid[i][j] == 1 : ans[i][j] = 0
                else : ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[r-1][c-1]