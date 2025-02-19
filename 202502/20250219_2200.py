## https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ln, ans = len(nums), []
        try : p = nums.index(key)
        except : return ans
        idx = max(p-k, 0)
        while True :
            while idx <= p+k and idx < ln:
                ans.append(idx)
                idx += 1
            try : p = nums[p+1:].index(key) + p + 1
            except : return ans
            idx = max(p-k, idx)
        return ans