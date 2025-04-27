## https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        lst, ans = [0 for i in range(25)], 0
        for hour in hours:
            h = hour % 24
            ans += lst[(24 - h) % 24]
            lst[h] += 1
        return ans

        # ln, ans = len(hours), 0
        # for i in range(ln-1):
        #     cnt, n = 0, (24 - (hours[i] % 24)) % 24
        #     for j in range(i+1, ln):
        #         if hours[j] % 24 == n: cnt += 1
        #     ans += cnt
        # return ans