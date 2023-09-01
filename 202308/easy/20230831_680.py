## https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.checking(s, 0)

    def checking(self, s, cnt) :
        stt, mid, end = 0, len(s)//2, len(s)-1
        while stt < mid :
            if s[stt] == s[end] :
                stt += 1
                end -= 1
            else :
                if cnt == 1 : return False
                if s[stt+1] != s[end] and s[stt] != s[end-1] : return False
                if s[stt+1] == s[end] :
                    if self.checking(s[stt+2:end], 1) == True : return True
                if s[stt] == s[end-1] :
                    if self.checking(s[stt+1:end-1], 1) == True : return True
                return False
        return True