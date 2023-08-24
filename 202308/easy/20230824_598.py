## https://leetcode.com/problems/range-addition-ii/

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == [] : return m * n
        return (min([o[0] for o in ops])) * (min([o[1] for o in ops]))