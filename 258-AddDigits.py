class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        result = num%10 + num//10
        if result < 10:
            return result
        else:
            return self.addDigits(result)

test = Solution()
print(test.addDigits(19))