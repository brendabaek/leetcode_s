## https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        lst, ans = [i for i in range(1, k+1)], 0
        while lst != [] :
            ans += 1
            try : lst.remove(nums.pop())
            except : pass
        return ans