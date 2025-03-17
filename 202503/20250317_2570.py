## https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        idx1, idx2, ln1, ln2, ans = 0, 0, len(nums1), len(nums2), []
        while idx1 < ln1 and idx2 < ln2 :            
            if nums1[idx1][0] < nums2[idx2][0] :
                ans.append(nums1[idx1]); idx1 += 1
            elif nums1[idx1][0] == nums2[idx2][0] :
                ans.append([nums1[idx1][0], (nums1[idx1][1] + nums2[idx2][1])])
                idx1 += 1; idx2 += 1
            else : ans.append(nums2[idx2]); idx2 += 1
        if idx1 < ln1 : ans += nums1[idx1:]
        if idx2 < ln2 : ans += nums2[idx2:]
        return ans