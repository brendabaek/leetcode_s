## https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.lstrip(' ').split(' ')[0]
        if len(word) == 0 : return 0

        try :
            ans = int(word)
            if ans < 0 : return max(-(2**31), ans)
            else : return min(((2**31)-1), ans)

        except :
            ans = ''
            cnt = 0
            if word[0] == '+' or word[0] == '-' :
                ans += word[0]
                word = word[1:]

            for i in word :
                try :
                    num = int(i)
                    ans = ans + i
                except : break

        try :
            ans = int(ans)
            if ans < 0 : return max(-(2**31), ans)
            else : return min(((2**31)-1), ans)
        except : return 0
