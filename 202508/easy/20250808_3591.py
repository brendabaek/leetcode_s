## https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        dics, lst = {}, []
        for num in nums:
            try: dics[num] += 1
            except: dics[num] = 1
        for v in dics.values():
            if v != 1: lst.append(v)
        if lst == []: return False
        for l in lst:
            c = True
            for i in range(2, l):
                if l % i == 0: c = False; break
            if c == True: return True
        return False