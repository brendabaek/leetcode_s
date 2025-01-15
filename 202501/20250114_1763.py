## https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ln, ans = len(s), ""
        for i in range(ln) :
            for j in range(i+2, ln+1) :
                check = True
                set_lists = set(s[i:j])
                for set_list in set_lists :
                    if set_list.swapcase() not in set_lists :
                        check = False
                        break
                if check == True and j-i > len(ans) : ans = s[i:j]
        return ans