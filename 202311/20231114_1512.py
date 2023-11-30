## https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dics = {}
        for num in nums :
            try : dics[num] += 1
            except : dics[num] = 1
        ans = 0
        for v in dics.values() :
            if v > 1 :
                for n in range(1, v) : ans += n
        return ans