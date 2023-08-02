## https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = []
        a = []
        ln = len(s)

        for l in s :
            if l in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] :
                v.append(l)
        
        for l in s :
            if l in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] :
                a.append(v.pop())
            else : a.append(l)
        
        ans = ''.join(a)

        return ans