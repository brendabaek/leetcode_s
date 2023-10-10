## https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dics = {}
        for c in chars :
            try : dics[c] += 1
            except : dics[c] = 1
        ans = 0
        for word in words :
            tmp, check = {}, True
            for w in word :
                try : tmp[w] += 1
                except : tmp[w] = 1
            for k, v in tmp.items() :
                try :
                    if tmp[k] <= dics[k] : pass
                    else :
                        check = False
                        break
                except :
                    check = False
                    break
            if check == True : ans += len(word)
        return ans