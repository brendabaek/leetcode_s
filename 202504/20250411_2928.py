## https://leetcode.com/problems/distribute-candies-among-children-i/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3: return 0
        elif n == limit * 3: return 1
        ans = 0
        for i in range(limit+1):
            t = n - i
            if t <= limit * 2 :
                for j in range(min(t+1, limit+1)):
                    if t - j <= limit: ans += 1
        return ans