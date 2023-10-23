## https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/


dics = {str(i+1):chr(i+97) for i in range(26)}

class Solution:
    def freqAlphabets(self, s: str) -> str:
        idx, ans = len(s)-1, ''
        while idx >= 0 :
            if s[idx] == '#' :
                ans = dics[s[idx-2:idx]] + ans
                idx -= 3
            else :
                ans = dics[s[idx]] + ans
                idx -= 1
        return ans