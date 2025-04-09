## https://leetcode.com/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans, idx = [], [], 0
        for num in nums :
            if num > 0 : idx = 0; seen = [num] + seen
            else :
                try : ans += [seen[idx]]; idx += 1
                except : ans += [-1]; idx += 1
        return ans