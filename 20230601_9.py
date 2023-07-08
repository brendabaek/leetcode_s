## https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        txt = str(x)
        forward = []
        reverse = []

        for t in txt :
            forward.append(t)
            reverse.insert(0, t)

        if forward == reverse :            
            return True
        else :
            return False