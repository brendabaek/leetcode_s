## https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(max(c) for c in zip(*[sorted(r) for r in grid]))

        # for g in grid : g.sort()
        # m, n, ans = len(grid), len(grid[0]), 0
        # new_grid = [set() for _ in range(n)]
        # for i in range(n) :
        #     for j in range(m) :
        #         new_grid[i].add(grid[j].pop())
        # for n in new_grid : ans += max(n)
        # return ans

        # m, n, ans = len(grid), len(grid[0]), 0
        # for i in range(n) :
        #     tmp = 0
        #     for j in range(m) : tmp = max(tmp, grid[j].pop())
        #     ans += tmp
        # return ans