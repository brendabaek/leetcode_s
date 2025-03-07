## https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        p, lst = 0, []
        for log in logs :
            lst.append(log[1]-p)
            p = log[1]
        m, ans = max(lst), []
        for i, v in enumerate(lst) :
            if v == m : ans.append(logs[i][0])
        return min(ans)