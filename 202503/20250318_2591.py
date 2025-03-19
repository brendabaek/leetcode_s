## https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children : return -1
        money -= children
        q, r = money // 7, money % 7
        if q == children and r == 0 : return children
        elif q == children and r > 0 : return max(children - 1, 0)
        elif q == children -1 and r != 3 : return q
        elif q == children -1 and r == 3 : return max(q - 1, 0)
        elif q < children - 1 : return q
        else : return children - 1