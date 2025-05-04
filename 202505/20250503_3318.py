## https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        dics, idx, ln, ans = {}, k - 1, len(nums), []
        for i in nums[:k - 1]:
            try: dics[i] += 1
            except: dics[i] = 1

        while idx < ln:
            try: dics[nums[idx]] += 1
            except: dics[nums[idx]] = 1
            dics = sorted(dics.items(), key=lambda x: (x[1], x[0]), reverse=True)
            top_x = list(dics)[:x]
            dics = dict(dics)
            tmp = 0
            for a, b in top_x: tmp += a * b
            ans.append(tmp)
            idx += 1
            dics[nums[idx-k]] -= 1
        return ans