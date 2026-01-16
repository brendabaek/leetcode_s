## https://leetcode.com/problems/sort-integers-by-binary-reflection/

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        dics = {}
        for i, num in enumerate(nums):
            dics[(num, i)] = int(bin(num)[-1:1:-1])
        dics = dict(sorted(dics.items(), key=lambda x: (x[1], x[0][0])))
        return [k[0] for k in dics.keys()]

        # test = sorted(dics.items(), key=lambda x: (x[1], x[0][0]))
        # return [k[0][0] for k in test]


        # reverse = lambda num: int(bin(num)[-1:1:-1], 2)
        # nums.sort(key = lambda x: (reverse(x), x))
        # return nums

        # return sorted(nums,key=lambda x:(int(bin(x)[2:][::-1]),x))