## https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ln, ans = len(startTime), 0
        for i in range(ln) :
            if startTime[i] <= queryTime and queryTime <= endTime[i] :
                ans += 1
        return ans