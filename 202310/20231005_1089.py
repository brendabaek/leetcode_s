## https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx, ln = 0, len(arr)
        while idx < ln :
            if arr[idx] == 0 :
                arr.insert(idx+1, 0)
                arr.pop()
                idx += 2
            else : idx += 1
        return arr