## https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right,  = 0, 1
        for _ in range(n) : left, right = right, left+right
        return left