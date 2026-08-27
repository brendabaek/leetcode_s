## https://leetcode.com/problems/minimum-capacity-box/

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n, ans = 100, -1
        for i in range(len(capacity)):
            if 0 <= capacity[i] - itemSize < n: n, ans = capacity[i] - itemSize, i
        return ans