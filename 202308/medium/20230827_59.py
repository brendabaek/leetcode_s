## https://leetcode.com/problems/spiral-matrix-ii/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num, cnt, r, c, ans = 1, n, 0, -1, [[0 for j in range(n)] for i in range(n)]
        
        while num <= n*n:
            for i in range(cnt) :
                if num > (n*n) : return ans
                c += 1
                ans[r][c] = num
                num += 1
            cnt -= 1
            
            for j in range(cnt) :
                if num > (n*n) : return ans
                r += 1
                ans[r][c] = num
                num += 1

            for k in range(cnt) :
                if num > (n*n) : return ans
                c -= 1
                ans[r][c] = num
                num += 1
            cnt -= 1
            
            for l in range(cnt) :
                if num > (n*n) : return ans
                r -= 1
                ans[r][c] = num
                num += 1
            
        if num > (n*n) : return ans