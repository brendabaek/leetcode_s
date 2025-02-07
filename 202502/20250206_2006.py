## https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dics = {}
        for num in nums :
            try : dics[num] += 1
            except : dics[num] = 1
        lst = sorted(dics)
        ans = 0
        for i in range(len(lst)) :
            if lst[i] + k in lst[i+1:] :
                ans += dics[lst[i]] * dics[lst[i]+k]
        return ans