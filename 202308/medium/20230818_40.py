## https://leetcode.com/problems/combination-sum-ii/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candid = []
        for c in candidates :
            if c <= target : candid.append(c)
        candid.sort()

        cand, pre = [], 0
        for c in candid :
            if c != pre :
                cand.append(c)
                pre, cnt = c, 1
            elif c == pre and cnt <= target :
                cand.append(c)
                cnt += 1
        
        if len(cand) == 0 : return
        elif sum(cand) < target : return
        return self.find_answer(cand, target, [], set())

    def find_answer(self, cand, target, tmp, ans) :
        if target == 0 :
            ans.add(tuple(tmp))
            return ans
        elif target < 0 : return ans
        elif sum(cand) < target : return ans
        for i in range(len(cand)) :
            ans = self.find_answer(cand[i+1:], target-cand[i], tmp+[cand[i]], ans)
        return ans