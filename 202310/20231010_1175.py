## https://leetcode.com/problems/prime-arrangements/

prime, nprime = [], [1]
for i in range(2, 101) :
    check = True
    for j in range(2, i) :
        if i % j == 0 :
            check = False
            nprime.append(i)
            break
    if check == True : prime.append(i)

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        p_cnt, np_cnt, ans = 0, 0, 1
        for i in range(1, n+1) :
            if i in prime : p_cnt += 1
            elif i in nprime : np_cnt += 1
        for i in range(1, p_cnt+1) : ans *= i
        for i in range(1, np_cnt+1) : ans *= i
        return ans % (10**9+7)