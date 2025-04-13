## https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ln, ans = len(nums), 151
        for i in range(ln-2) :
            if nums[i] < ans - 3 :
                n1 = nums[i]
                t1 = ans - n1 - 1
                for j in range(i+1, ln-1) :
                    if nums[j] > n1 and nums[j] < t1 :
                        n2 = nums[j]
                        t2 = ans - n1 - n2
                        for k in range(j+1, ln) :
                            if nums[k] < n2 and nums[k] < t2 : ans = min(ans, n1+n2+nums[k])
        return -1 if ans == 151 else ans