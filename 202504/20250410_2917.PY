## https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        dics, ans = {i:0 for i in range(len(bin(max(nums)))-2)}, ""
        for num in nums:
            bi = bin(num)[2:][::-1]
            for idx, b in enumerate(bi):
                if b == "1": dics[idx] += 1
        for v in dics.values() :
            if v < k : ans = "0" + ans
            else : ans = "1" + ans
        return int(ans, 2)