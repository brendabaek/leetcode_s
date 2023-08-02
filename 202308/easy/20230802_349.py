## https://leetcode.com/problems/intersection-of-two-arrays/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for n1 in nums1 :
            if n1 not in ans :
                for n2 in nums2 :
                    if n2 not in ans :
                        if n1 == n2 :
                            ans.append(n1)
        
        return ans