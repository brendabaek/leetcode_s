## https://leetcode.com/problems/limit-occurrences-in-sorted-array/

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        dics, ans = {}, []
        for num in nums:
            try: dics[num] += 1
            except: dics[num] = 1
        for k, v in dics.items(): ans += [k] * min(v, k)
        return ans