## https://leetcode.com/problems/day-of-the-week/

mn = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
date = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        nums = day
        for i in range(1, month) : nums += mn[i]
        for y in range(1971, year) :
            if y % 100 == 0 and y % 400 != 0 : nums += 365
            elif y % 4 == 0 : nums += 366
            else : nums += 365
        if ((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)) and month > 2 : nums += 1
        return date[nums%7]