## https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        p, ans = 0, []
        for i in range(m - 1):
            if p < n - 1:
                r = "#" * p + ".." + "#" * (n - 2 - p)
                p += 1
            else: r = "#" * p + "."
            ans.append(r)
        ans.append("#" * p + "." * (n - p))
        return ans