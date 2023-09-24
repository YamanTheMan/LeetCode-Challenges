class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        if x < 0 or (x % 10 == 0 and n != 0):
            return False
        rev = 0
        while x != 0:
            rev = rev*10 + x % 10
            x //= 10
        if rev == n:
            return True
        else:
            False
