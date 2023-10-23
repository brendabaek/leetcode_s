## https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ln, pre, ans = len(arr), 0, []
        for i in range(0, ln-1) :
            if arr[i] > pre or arr[i] == ans[-1] : ans.append(max(arr[i+1:]))
            else : ans += [ans[-1]]
            # if arr[i] <= pre and arr[i] < ans[-1] : ans += [ans[-1]]
            # else : ans.append(max(arr[i+1:]))
            pre = arr[i]
        return ans + [-1]