## https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        # for num in nums :
        #     num = str(num)
        #     for n in num : ans.append(int(n))
        # return ans

        # for num in nums :
        #     tmp = []
        #     while num > 0 :
        #         tmp.append(num % 10)
        #         num //= 10
        #     ans += tmp[::-1]
        # return ans

        for num in nums :
            idx = len(ans)
            while num > 0 :
                ans.insert(idx, num % 10)
                num //= 10
        return ans