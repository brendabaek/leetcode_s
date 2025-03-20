## https://leetcode.com/problems/prime-in-diagonal/

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ln, lst = len(nums), set()
        for i in range(ln) :
            lst.add(nums[i][i])
            lst.add(nums[ln-1-i][i])
        lst = list(lst)
        lst.sort(reverse=True)
        for num in lst :
            if num == 1 : break
            check = True
            for n in range(2, int(num ** 0.5) + 1) :
                if num % n == 0 : check = False; break
            if check == True : return num
        return 0