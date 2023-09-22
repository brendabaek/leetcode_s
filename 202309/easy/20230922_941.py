## https://leetcode.com/problems/valid-mountain-array/

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        idx, ln = 0, len(arr)
        while idx < ln-1 and arr[idx] < arr[idx+1] : idx += 1
        if idx == 0 or idx == ln-1 : return False
        while idx < ln-1 and arr[idx] > arr[idx+1] : idx += 1
        return idx == ln-1