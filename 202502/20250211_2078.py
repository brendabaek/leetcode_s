## https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        s, ln, ans = 0, len(colors) - 1, 0
        while ln - s > ans :
            e = ln
            while e - s > ans :
                if colors[s] != colors[e] :
                    ans = max(ans, abs(s - e))
                    break
                else : e -= 1
            s += 1
        return ans