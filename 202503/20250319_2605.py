## https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(), nums2.sort()
        for num in nums1 :
            if num in nums2 : return num
        if nums1[0] < nums2[0] : return (nums1[0] * 10) + nums2[0]
        else : return (nums2[0] * 10) + nums1[0]