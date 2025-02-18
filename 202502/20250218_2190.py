## https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        ln, dics = len(nums),{}
        for i in range(ln-1) :
            if nums[i] == key :
                try : dics[nums[i+1]] += 1
                except : dics[nums[i+1]] = 1
        return max(dics, key = dics.get)