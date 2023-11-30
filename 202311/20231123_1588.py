## https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ln, ans = len(arr), 0
        lst = [0 for _ in range(ln)]
        if ln % 2 == 0 :
            h = ln // 2
            for i in range(1, h+1) :
                for j in range(1, h+1) :
                    lst[j-1] = lst[j-1] + min(i, j)
                    lst[-j] = lst[-j] + min(i, j)
        else :
            h = ln // 2 + 1
            for i in range(1, h+1, 2) :
                for j in range(1, h+1) :
                    if i == h :
                        if j == h :
                            lst[j-1] = lst[j-1] + min(i, j)
                        else :
                            lst[j-1] = lst[j-1] + min(i, j)
                            lst[-j] = lst[-j] + min(i, j)
                    else :
                        if j == h :
                            lst[j-1] = lst[j-1] + (min(i, j) *2)
                        else :
                            lst[j-1] = lst[j-1] + (min(i, j) *2)
                            lst[-j] = lst[-j] + (min(i, j) *2)
        for k in range(ln) : ans += arr[k] * lst[k]
        return ans