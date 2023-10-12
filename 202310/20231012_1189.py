## https://leetcode.com/problems/maximum-number-of-balloons/

balloon = {"b" : 1, "a" : 1, "l" : 2, "o" : 2, "n" : 1}

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = {"b" : 0, "a" : 0, "l" : 0, "o" : 0, "n" : 0}
        for t in text :
            if t in cnt : cnt[t] += 1
        ans = 0
        while True :
            for k, v in balloon.items() :
                if cnt[k] - v >= 0 : cnt[k] -= v
                else : return ans
            ans += 1
        return ans