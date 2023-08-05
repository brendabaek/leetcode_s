## https://leetcode.com/problems/binary-watch/

h = {i:[] for i in range(4)}
m = {i:[] for i in range(6)}
for i in range(12) : h[bin(i).count("1")].append(str(i))
for i in range(60) :
    if i < 10 : m[bin(i).count("1")].append(":0"+str(i))
    else : m[bin(i).count("1")].append(":"+str(i))

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """       
        if turnedOn >= 9 : return

        ans = []
        for i in range(min((turnedOn+1), 4)) :
            j = turnedOn - i
            if j >= 6 : continue
            for hour in h[i] :
                for minute in m[j] :
                    ans.append(hour+minute)
        
        return ans