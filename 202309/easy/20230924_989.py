## https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = 0
        for n_ in num : n = (n * 10) + n_
        n, ans = n + k, []
        while n > 0 :
            ans.insert(0, n%10)
            n = n // 10
        return ans