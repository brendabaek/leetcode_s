## https://leetcode.com/problems/alternating-groups-i/

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c1, c2, c3, ans = colors[-3], colors[-2], colors[-1], 0
        for i in range(0, len(colors)):
            c1, c2, c3 = c2, c3, colors[i]
            if c1 != c2 and c2 != c3: ans += 1
        return ans