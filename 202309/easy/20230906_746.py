## https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        sum1, sum2 = cost[0], cost[1]
        for i in range(2, len(cost)) :
            if cost[i] + sum1 > cost[i] + sum2 :
                sum1, sum2 = sum2, sum2+cost[i]
            else : sum1, sum2 = sum2, sum1+cost[i]
        return min(sum1, sum2)                