## https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ln, idx, ans = len(arr), 0, 0
        while idx < ln :
            ans += 1
            if arr[idx] == ans : idx += 1
            else :
                k -= 1
                if k == 0 : return ans
        return ans + k