## https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        ln = len(arr)
        for i in range(ln-(m*k)+1) :
            a = arr[i:i+(m*k)]
            s = a[:m]
            c = True
            for j in range(k-1) :
                if a[m*(j+1):m*(j+2)] != s :
                    c = False
                    break
            if c : return True
        return False