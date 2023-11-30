## https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        s = max(candies)-extraCandies
        for c in candies :
            if c >= s : ans.append(True)
            else : ans.append(False)
        return ans