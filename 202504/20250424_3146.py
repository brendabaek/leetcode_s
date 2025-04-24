## https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dics, ans = {}, 0
        for idx1, l1 in enumerate(s): dics[l1] = idx1
        for idx2, l2 in enumerate(t): ans += abs(dics[l2] - idx2)
        return ans

        # dics = {}
        # for idx1, l1 in enumerate(s): dics[l1] = idx1
        # for idx2, l2 in enumerate(t): dics[l2] = abs(dics[l2] - idx2)
        # return sum(dics.values())

        # ln, ans = len(s), 0
        # for i in range(ln): ans += abs(i - t.index(s[i]))
        # return ans