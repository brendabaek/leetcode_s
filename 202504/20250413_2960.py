## https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans, cnt = 0, 0
        for b in batteryPercentages :
            if b - cnt > 0 : cnt += 1; ans += 1
        return ans