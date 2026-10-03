## https://leetcode.com/problems/count-integers-appearing-in-a-single-block/

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dics = {}
        for i in range(len(nums)):
            if nums[i] not in dics: dics[nums[i]] = [i]
            else:
                if dics[nums[i]] == False: pass
                elif dics[nums[i]][-1] + 1 == i: dics[nums[i]].append(i)
                else: dics[nums[i]] = False
        return sum(bool(v) for v in dics.values())