## https://leetcode.com/problems/assign-cookies/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if s == [] : return 0

        g.sort()
        s.sort()
        ln1, ln2 = len(g), len(s)
        cnt1, cnt2, ans = 0, 0, 0

        while cnt1 < ln1 and cnt2 < ln2 :
            if g[cnt1] <= s[cnt2] :
                cnt1 += 1
                cnt2 += 1
                ans += 1
            else : cnt2 += 1
        return ans