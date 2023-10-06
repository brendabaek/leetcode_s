## https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        idx, c, ans = 0, 1, [0] * num_people
        while candies > 0:
            if idx == num_people : idx = 0
            ans[idx] = ans[idx] + min(candies, c)
            candies -= c
            idx += 1
            c += 1            
        return ans