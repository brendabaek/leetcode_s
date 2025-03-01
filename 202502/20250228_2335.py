## https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse = True)
        if amount[0] >= amount[1] + amount[2]  : return amount[0]
        return amount[2] + amount[1] - (amount[2]-(amount[0]-amount[1])) // 2