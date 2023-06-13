## https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        
        for i in range(len(s)-1, -1 , -1) :
            if len(s[i]) > 0 : return len(s[i])
        return 0