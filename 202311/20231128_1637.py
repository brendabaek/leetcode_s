## https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        s, ans = set(), 0
        for p in points : s.add(p[0])
        lst = sorted(list(s))
        pre = lst[0]
        for l in lst[1:] :
            ans = max(l-pre, ans)
            pre = l
        return ans