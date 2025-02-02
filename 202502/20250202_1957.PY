## https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt, ans = 1, s[0]
        for i in s[1:] :
            if i == ans[-1] :
                if cnt == 2 : continue
                else : cnt, ans = cnt + 1, ans + i
            else : cnt, ans = 1, ans + i
        return ans