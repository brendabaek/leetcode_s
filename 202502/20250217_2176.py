## https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dics, ans = {}, 0
        for i in range(len(nums)) :
            try : dics[nums[i]].append(i)
            except : dics[nums[i]] = [i]
        for v in dics.values() :
            if len(v) > 1 :
                for j in range(len(v)-1) :
                    for l in range(j+1, len(v)) :
                        if (v[j] * v[l]) % k == 0 : ans += 1
        return ans