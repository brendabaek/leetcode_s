## https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        ln2 = len(nums2)
        for n1 in nums1 :
            idx = nums2.index(n1)
            if idx == ln2-1 : ans.append(-1)
            else :
                for i in range(idx+1, ln2) :
                    if nums2[i] > n1 :
                        ans.append(nums2[i])
                        break
                    if i == ln2-1 : ans.append(-1)
        return ans