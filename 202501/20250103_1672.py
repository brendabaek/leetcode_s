## https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m, n = len(accounts), len(accounts[0])
        sums, mx = 0, 0
        for i in range(m) :
            for j in range(n) :
                sums += accounts[i][j]
            mx = max(sums, mx)
            sums = 0
        return mx