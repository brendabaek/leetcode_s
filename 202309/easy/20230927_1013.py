## https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        avg = sum(arr)/3

        ln, sum1, sum2, sum3 = len(arr), 0, 0, 0
        for i in range(ln-2) :
            sum1 += arr[i]
            if sum1 == avg :
                for j in range(ln-1, i, -1) :
                    sum3 += arr[j]
                    if sum3 == avg : sum2 = sum(arr[i+1:j])
                    if i+1 < j and sum1 == avg and sum2 == avg and sum3 == avg : return True
        return False