## https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ln = len(s)
        if ln < 2 : return s
        ans = ''
        for i in range(ln-1) :
            for j in range(ln-1, i, -1) :
                if s[i] != s[j] :
                    continue
                else :
                    for m in range(((j-i)//2)+1) :
                        if s[i+m] != s[j-m] :
                            break
                        else :
                            if (j-m)-(i+m) < 2 :
                                if len(s[i:j+1]) > len(ans) :
                                    ans = s[i:j+1]
                                if j == ln-1 : return ans
                            else : continue

                    if ((i+j) // 2) == 0 :
                        if len(s[i:j+1]) > len(ans) :
                            ans = s[i:j+1]
        if ans == '' : ans = s[0]
        return ans



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ln = len(s)
        if ln < 2 : return s

        ans = ''
        for i in range(ln) :
            stt, end = i, i
            while stt >= 0 and end < ln and s[stt] == s[end]:
                tmp = s[stt:end+1]
                stt -= 1
                end += 1
            if len(ans) < len(tmp) : ans = tmp

        for i in range(ln) :
            stt, end = i, i+1
            while stt >= 0 and end < ln and s[stt] == s[end]:
                tmp = s[stt:end+1]
                stt -= 1
                end += 1
            if len(ans) < len(tmp) : ans = tmp
        return ans