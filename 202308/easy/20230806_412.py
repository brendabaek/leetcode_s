## https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        num = 0
        for i in range(n//15) :
            lst = [str(num+1), str(num+2), "Fizz", str(num+4), "Buzz",
                "Fizz", str(num+7), str(num+8), "Fizz", "Buzz",
                str(num+11), "Fizz", str(num+13), str(num+14),"FizzBuzz"]
            ans += lst
            num += 15

        lst = [str(num+1), str(num+2), "Fizz", str(num+4), "Buzz",
            "Fizz", str(num+7), str(num+8), "Fizz", "Buzz",
            str(num+11), "Fizz", str(num+13), str(num+14),"FizzBuzz"]

        ans += lst[:(n%15)]
        return ans