## https://leetcode.com/problems/elevator-requests-i/

class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        c, ans = 0, 0
        for r in requests:
            ans += abs(c - r)
            c = r
        return ans