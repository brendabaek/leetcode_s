## https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1 : return
        ln = len(s)        
        for i in range(ln-2, -1, -1) :
            s.append(s.pop(i))
        return