## https://leetcode.com/problems/distance-between-bus-stops/

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination : start, destination = destination, start
        pos = sum(distance[start:destination])
        neg = sum(distance[:start])+sum(distance[destination:])
        return min(pos, neg)