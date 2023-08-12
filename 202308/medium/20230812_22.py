## https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = ["()"]
        tmp = []
        
        for _ in range(n-1) :
            for a in ans :
                for i in range(a.find(")")+1) :
                    t = a[:i] + "()" + a[i:]
                    tmp.append(t)
            ans = tmp
            tmp = []

        return ans