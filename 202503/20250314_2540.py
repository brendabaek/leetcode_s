## https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1, idx2, ln1, ln2 = 0, 0, len(nums1), len(nums2)
        while idx1 < ln1 and idx2 < ln2 :
            if nums1[idx1] == nums2[idx2] : return nums1[idx1]
            elif nums1[idx1] < nums2[idx2] : idx1 += 1
            else : idx2 += 1
        return -1