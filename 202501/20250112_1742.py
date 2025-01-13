## https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = {}
        for i in range(lowLimit, highLimit+1) :
            sums = 0
            for j in str(i) : sums += int(j)
            try : ans[sums] += 1
            except : ans[sums] = 1
        return max(ans.values())