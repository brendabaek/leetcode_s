## https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for num in arr2 :
            while num in arr1 :
                ans.append(num)
                arr1.remove(num)
        arr1.sort()
        ans += arr1
        return ans