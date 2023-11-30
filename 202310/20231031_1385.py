## https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for a1 in arr1 :
            ans += 1
            for a2 in arr2 :
                if abs(a1-a2) <= d :
                    ans -= 1
                    break
        return ans