## https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ln, dics, ans = len(nums), {}, []
        for num in nums :
            for n in num :
                try : dics[n] += 1
                except : dics[n] = 1
        for k, v in dics.items() :
            if v == ln : ans.append(k)
        ans.sort()
        return ans