class Solution:
    def reverse(self, x):
        sign = -1 if x<0 else 1
        x = int(str(abs(x))[::-1])
        return sign*x if -2**31 <= sign*x <= 2**31-1 else 0