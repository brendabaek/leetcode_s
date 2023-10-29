## https://leetcode.com/problems/increasing-decreasing-string/

class Solution:
    def sortString(self, s: str) -> str:
        lst, ans = list(s), []
        while len(lst) > 0 :
            s_lst = sorted(set(lst))
            ans += s_lst
            for l in s_lst : lst.remove(l)
            s_lst = sorted(set(lst))[::-1]
            ans += s_lst
            for l in s_lst : lst.remove(l)
        return ''.join(ans)