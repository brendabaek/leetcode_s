## https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n, c = arr[0], arr[1] - arr[0]
        for a in arr :
            if n == a : n += c
            else : return False
        return True