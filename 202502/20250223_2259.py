## https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        f_idx, e_idx = number.index(digit), len(number) - 1 - number[::-1].index(digit)
        while f_idx < e_idx :
            if number[f_idx+1] > number[f_idx] : return number[:f_idx] + number[f_idx+1:]
            f_idx = f_idx + 1 + number[f_idx+1:].index(digit)
        return number[:e_idx] + number[e_idx+1:]