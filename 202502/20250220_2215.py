## https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2, ans = set(nums1), set(nums2), []
        for num in nums1 :
            if num in nums2 : nums2.remove(num)
            else : ans.append(num)
        return [ans, list(nums2)]