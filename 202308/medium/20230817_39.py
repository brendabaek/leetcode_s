## https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        cand = []
        for c in candidates :
            if c <= target : cand.append(c)
        ln = len(cand)
        if ln == 0 : return
        cand.sort()
        return self.find_sum(cand, target, [], [])

    def find_sum(self, cand, target, tmp, ans) :
        if target < 0 : return ans
        if target == 0 :
            ans.append(tmp)
            return ans
        for i in range(len(cand)) :
            self.find_sum(cand[i:], target-cand[i], tmp+[cand[i]], ans)
        return ans