## https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dics, ans = {}, 0
        for i in range(len(nums)):
            if nums[i] in dics: dics[nums[i]].append(i)
            else: dics[nums[i]] = [i]
        for v in dics.values():
            if len(v) == 3 and v[1] - v[0] == v[2] - v[1]: ans += 1
        return ans