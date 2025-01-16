## https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # ans = ""
        # if len(word2) > len(word1) :
        #     for i in range(len(word1)) : ans = ans + word1[i] + word2[i]
        #     ans += word2[len(word1):]
        # else :
        #     for i in range(len(word2)) : ans = ans + word1[i] + word2[i]
        #     ans += word1[len(word2):]
        # return ans

        for i in range(len(word2)) :
            try : word1 = word1[:2*i+1] + word2[i] + word1[2*i+1:]
            except :
                word1 = word1 + word2[i:]
                break
        return word1