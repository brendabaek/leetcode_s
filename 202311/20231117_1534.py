## https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ln, ans = len(arr), 0
        for i in range(ln-2) :
            for j in range(i+1, ln-1) :
                for k in range(j+1, ln) :
                    if abs(arr[i]-arr[j]) <= a and \
                        abs(arr[j]-arr[k]) <= b and \
                        abs(arr[k]-arr[i]) <= c :
                        ans += 1
        return ans