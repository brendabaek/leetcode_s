## https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dics, ans = {}, 0
        for num in nums:
            try: dics[num] += 1
            except: dics[num] = 1
        max_f = max(dics.values())
        for v in dics.values():
            if v == max_f : ans += v
        return ans