## https://leetcode.com/problems/day-of-the-year/

dics = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

class Solution:
    def dayOfYear(self, date: str) -> int:
        yr, mn, ans = int(date[:4]), int(date[5:7]), int(date[8:])
        for i in range(1, mn) : ans += dics[i]
        if yr % 400 == 0 and mn > 2 : ans += 1
        elif yr % 100 != 0 and yr % 4 == 0 and mn > 2 : ans += 1
        return ans