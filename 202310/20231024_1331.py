## https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dics, ln = {}, len(arr)
        for i in range(ln) : dics[i] = arr[i]
        cnt, pre, ans = 1, None, [0] * ln
        for i in sorted(dics, key=dics.get) :
            if arr[i] == pre : ans[i] = cnt-1
            else :
                ans[i] = cnt
                pre = arr[i]
                cnt += 1
        return ans