## https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans, dics = -1, {}
        for i in range(len(nums)) :
            n, num = 0, nums[i]
            while num > 0 : n = max(n, num % 10); num //= 10
            try : dics[n].append(nums[i])
            except : dics[n] = [nums[i]]
        dics = dict(sorted(dics.items(), key=lambda x: x[0], reverse=True))
        for k, v in dics.items() :
            if len(v) < 2 : continue
            else :
                tmp = max(v); v.remove(tmp)
                tmp += max(v); ans = max(ans, tmp)
        return ans