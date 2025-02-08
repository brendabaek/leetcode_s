## https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        dics, ans = {}, []
        for n in nums :
            try : dics[n] += 1
            except : dics[n] = 1
        for k, v in dics.items() :
            if v > 1 : ans.append(k)
        return ans