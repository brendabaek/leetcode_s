## https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            n = str(num)
            l = len(n)
            ans += int(max(n) * l)
        return ans