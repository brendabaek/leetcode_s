## https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ln, n1, n2, n3 = len(arr), 0, 0, 0
        for i in range(ln) :
            if arr[i] % 2 == 0 : n1, n2, n3 = 0, 0, 0
            else : n1, n2, n3 = 1, n1, n2
            if n1 and n2 and n3 : return True
        return False