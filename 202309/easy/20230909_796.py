## https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)) :
            if s[i] == goal[0] :
                new_s = s[i:] + s[:i]
                if new_s == goal : return True
        return False