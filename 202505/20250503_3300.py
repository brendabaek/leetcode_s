## https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution:
    def minElement(self, nums: List[int]) -> int:
        # return min(sum(map(int, str(x))) for x in nums)

        # ans = 99999
        # for num in nums:
        #     nu = str(num)
        #     tmp = 0
        #     for n in nu:
        #         if tmp >= ans: break
        #         tmp += int(n)
        #     ans = min(ans, tmp)
        # return ans

        # ans = 99999
        # for num in nums:
        #     tmp = 0
        #     while num > 0:
        #         tmp += num % 10
        #         num //= 10
        #         if tmp >= ans: break
        #     if num == 0: ans = min(ans, tmp)
        # return ans

        nums.sort()
        d, tmp_d, ans = 0, 0, 99999
        for num in nums:
            if tmp_d == d and ans * (10 ** (d - 1)) <= num and num < (10 ** d): continue
            tmp_d, tmp = 0, 0
            while num > 0: tmp += num % 10; tmp_d += 1; num //= 10
            ans = min(ans, tmp)
            if tmp_d != d: d = tmp_d
        return ans