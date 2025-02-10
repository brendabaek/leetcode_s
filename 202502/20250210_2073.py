## https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target, ans = tickets[k], 0
        for i in range(k+1) :
            if tickets[i] <= target : ans += tickets[i]
            else : ans += target
        for j in range(k+1, len(tickets)) :
            if tickets[j] < target : ans += tickets[j]
            else : ans += target - 1
        return ans