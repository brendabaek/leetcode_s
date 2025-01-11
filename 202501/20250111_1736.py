## https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == "?" :
            if time[1] in "?0123": time = time.replace("?", "2", 1)
            else : time = time.replace("?", "1", 1)
        if time[1] == "?" :
            if time[0] == "2" : time = time.replace("?", "3", 1)
            else : time = time.replace("?", "9", 1)
        if time[3] == "?" : time = time.replace("?", "5", 1)
        if time[4] == "?" : time = time.replace("?", "9", 1)
        return time