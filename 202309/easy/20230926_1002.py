## https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dics, ans, ln = {}, [], len(words)
        for w in words[0] :
            try : dics[w] += 1
            except : dics[w] = 1
        
        for i in range(1, ln) :
            tmp = {}
            for w in words[i] :
                try : tmp[w] += 1
                except : tmp[w] = 1
            for k, v in dics.items() :
                try : dics[k] = min(dics[k], tmp[k])
                except : dics.pop(k)

        for k, v in dics.items() :
            for _ in range(v) : ans.append(k)
        return ans