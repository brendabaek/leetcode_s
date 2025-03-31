## https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 < 5 : return (10 - purchaseAmount // 10) * 10
        else : return ((10 - purchaseAmount // 10) - 1) * 10