## https://leetcode.com/problems/can-place-flowers/

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt, ans = 2, 0
        for i in range(len(flowerbed)-1) :
            if flowerbed[i] == 1 and flowerbed[i+1]  == 0 : cnt = 1
            elif flowerbed[i] == 0 and flowerbed[i+1]  == 0 : cnt += 1
            elif flowerbed[i] == 1 and flowerbed[i+1]  == 1 : cnt = 0
            else : ## flowerbed[i] == 0 and flowerbed[i+1]  == 1
                ans += (cnt-1) // 2
                cnt = 0
        ans += cnt // 2

        if len(flowerbed) == 1 : ans = 1-flowerbed[0]
        return n <= ans