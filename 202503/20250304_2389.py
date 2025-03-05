## https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ln, s, sums, ans = len(nums),  0, [], []
        for n in nums :
            s = s + n
            sums.append(s)
        for q in queries :
            idx = 0
            while idx < ln :
                if sums[idx] > q : ans.append(idx); break
                elif idx == ln - 1 : ans.append(idx+1); break
                else : idx += 1
        return ans