## https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if low > high : return 0
        ans = 0
        if low < 11 : low = 11
        while low < 100 and low <= high :
            if low // 10 == low % 10 : ans += 1; low += 11
            elif low // 10 < low % 10 : low = (((low // 10) + 1) * 10) + ((low // 10) + 1)
            else : low = ((low // 10) * 10) + (low // 10)
        if low > high : return ans
        low = max(low, 1001)
        while low <= high :
            o, t, f = (low // 1000) + ((low // 100) % 10), ((low % 100) // 10), low % 10
            if o == t + f : ans += 1; low += 9
            elif o < t : low = (((low // 100) + 1) * 100) + (o + 1)
            else :
                while o != ((low % 100) // 10) + (low % 10) : low += 1
        return ans