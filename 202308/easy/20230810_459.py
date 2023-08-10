## https://leetcode.com/problems/repeated-substring-pattern/

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]
    

        letter = ''
        ln = len(s)

        for i in range(ln) :
            if s[i] not in letter : letter += s[i]

            else :
                l = len(letter)
                cnt = 0
                if i+cnt+l > ln : return False
                while i+cnt+l <= ln :
                    if letter == s[i+cnt:i+cnt+l] :
                        if i+cnt+l == ln : return True
                        else : cnt += l
                    else :
                        letter += s[i]
                        break                
        return False
