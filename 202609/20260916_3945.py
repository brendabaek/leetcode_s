## https://leetcode.com/problems/digit-frequency-score/

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dics, ans = {}, 0
        while n > 0:
            num, n = n % 10, n // 10
            try: dics[num] += 1
            except: dics[num] = 1
        for k, v in dics.items(): ans += k * v
        return ans