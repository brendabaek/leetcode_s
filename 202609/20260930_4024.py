## https://leetcode.com/problems/nearest-available-drone/

class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        idx, dist, ans = 0, 123, -1
        for drone in drones:
            d = abs(drone[0] - target[0]) + abs(drone[1] - target[1])
            if d <= drone[2] and d < dist:
                dist, ans = d, idx
            idx += 1
        return ans