## https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        dics, ans = {}, []
        for word in words :
            try : dics[len(word)].append(word)
            except : dics[len(word)] = [word]
        # dics = dict(sorted(dics.items()))

        for i in dics.keys() :
            for j in dics.keys() :
                if i > j :
                    for k in dics[j] :
                        for l in dics[i] :
                            if k in l :
                                ans.append(k)
                                
        return set(ans)