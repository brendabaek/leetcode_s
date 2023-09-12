## https://leetcode.com/problems/gray-code/

ans = [0]
for i in range(16) : ans += [ j + 2 ** i for j in ans[::-1]]

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return ans[:2**n]