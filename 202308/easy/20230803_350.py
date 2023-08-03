## https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for n1 in nums1 :
            if n1 in nums2 :
                ans.append(n1)
                nums2.remove(n1)

        return ans