## https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for n1 in nums1:
            if n1 % k == 0:
                n1 = n1 // k
                for n2 in nums2:
                    if n1 % n2 == 0: ans += 1        
        return ans