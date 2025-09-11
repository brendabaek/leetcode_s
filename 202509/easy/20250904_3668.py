## https://leetcode.com/problems/restore-finishing-order/

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for i in order:
            if i in friends:
                ans.append(i);
                friends.remove(i)
                if friends == []: return ans
        return ans