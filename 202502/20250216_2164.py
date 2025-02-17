## https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e, o, ans = [], [], []
        while nums != [] :
            e.append(nums.pop(0))
            if nums != [] : o.append(nums.pop(0))
        e.sort(), o.sort(reverse=True)
        while e != [] or o != [] :
            ans.append(e.pop(0))
            if o != [] : ans.append(o.pop(0))
        return ans