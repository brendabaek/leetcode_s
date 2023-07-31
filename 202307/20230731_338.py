## https://leetcode.com/problems/counting-bits/

ans_lst = [0, 1, 1, 2]
for _ in range(17) :
    ans_lst = ans_lst + [i+1 for i in ans_lst]

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return ans_lst[:n+1]