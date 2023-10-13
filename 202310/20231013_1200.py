## https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        idx, ln, dis, ans = 1, len(arr), arr[-1]-arr[0], []
        while idx < ln :
            d = arr[idx] - arr[idx-1]
            if d < dis :
                ans = [[arr[idx-1], arr[idx]]]
                dis = d
            elif d == dis : ans.append([arr[idx-1], arr[idx]])
            idx += 1
        return ans