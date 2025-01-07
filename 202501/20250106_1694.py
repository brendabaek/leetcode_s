## https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        cnt, ans = 0, ''
        for n in number :
            if n == ' ' or n == '-' : pass
            else :
                if cnt == 3 :
                    ans = ans + '-' + n
                    cnt = 1
                else :
                    ans = ans + n
                    cnt += 1
        if ans[-2] == '-' : return ans[:-3] + '-' + ans[-3] + ans[-1]
        return ans