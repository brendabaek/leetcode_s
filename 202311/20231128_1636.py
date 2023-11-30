## https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt, dics, ans = Counter(nums), {}, []
        for k, v in cnt.items() :
            try : dics[v].append(k)
            except : dics[v] = [k]
        for k in dics.keys() : dics[k] = sorted(dics[k])
        dics = dict(sorted(dics.items(), reverse=True))
        for k, v in dics.items() :
            for n in v : ans = [n] * k + ans
        return ans