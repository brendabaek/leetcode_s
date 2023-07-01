## https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        strs = re.sub('[^a-z0-9]', '', s.lower())
        ln = len(strs)

        if ln <= 1 : return True

        if ln % 2 == 0 :
            for i in range(ln//2) :
                if strs[i] == strs[-1-i] : continue
                else : return False
        else :
            for i in range(ln/2) :
                if strs[i] == strs[-1-i] : continue
                else : return False
        return True


