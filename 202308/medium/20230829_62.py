## https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = [[1] * n] * m
        for i in range(1, m) :
            for j in range(1, n) :
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[m-1][n-1]