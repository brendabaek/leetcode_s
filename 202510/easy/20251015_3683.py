## https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = sum(tasks[0])
        for t in tasks[1:]:
            if sum(t) < ans: ans = sum(t)
        return ans