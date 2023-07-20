## https://leetcode.com/problems/summary-ranges/

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0 : return
        ans , stt, end, crt = [], nums[0], None, 0

        for n in nums :
            if n != stt + crt : end = stt + crt - 1
            crt += 1
            if stt != None and end != None :
                if stt == end : rng = str(stt)
                else : rng = str(stt) + "->" + str(end)
                ans.append(rng)
                stt, end, crt = n, None, 1
        if stt == nums[-1] : rng = str(stt)
        else : rng = str(stt) + "->" + str(nums[-1])
        ans.append(rng)
        return ans