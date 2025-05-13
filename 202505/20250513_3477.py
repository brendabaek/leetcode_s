## https://leetcode.com/problems/fruits-into-baskets-ii/

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for f in fruits:
            check = False
            for i in range(len(baskets)):
                if f <= baskets[i]: baskets.pop(i); check = True; break
            if check == False: ans += 1
        return ans