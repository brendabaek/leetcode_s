## https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dics, ans = {}, 0
        for num in nums:
            try: dics[num] += 1
            except: dics[num] = 1
        for key, v in dics.items():
            if v % k == 0: ans += key * v
        return ans