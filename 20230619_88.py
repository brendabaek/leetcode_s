## https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if n == 0 : return nums1
        elif m == 0 :
            for j in range(n) :
                nums1.insert(j, nums2[j])
                nums1.pop()
            return nums1

        else :
            for zero in range(m, len(nums1)) : nums1.pop()

            for i in range(m+n) :
                if len(nums2) == 0 : return nums1

                if i < len(nums1) :    
                    if nums1[i] > nums2[0] :
                        nums1.insert(i, nums2[0])
                        nums2.pop(0)
                else :
                    nums1.append(nums2[0])
                    nums2.pop(0)

                    