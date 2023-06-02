class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        maps = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        nums=[]

        for i in s:
            nums.insert(0, maps[i])
        
        ln = len(nums)
        ans = 0
        r = 0

        for n in range(ln) :
            print(n)
            if nums[n] >= r :
                ans = ans + nums[n]
                r = nums[n]

            else :
                ans = ans - nums[n]
                r = nums[n]

        return ans