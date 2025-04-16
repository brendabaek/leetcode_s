## https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = [0 for _ in range(len(grid)**2)]
        for g in grid:
            for n in g: c[n-1] += 1
        return [c.index(2) + 1, c.index(0) + 1]

        # lst, ans1, ans2, c = [], 0, 0, 1
        # for g in grid:
        #     for n in g: lst.append(n)
        # lst.sort()
        # for l in lst :
        #     if c > l : ans1 = l
        #     elif c < l : ans2 = c; c += 2
        #     else : c += 1
        # return [ans1, ans2] if ans2 != 0 else [ans1, len(grid)**2]