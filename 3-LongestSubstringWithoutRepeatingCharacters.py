class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        start = 0
        result = 0
        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] >= start:
                start = hash_map[s[i]] + 1
            hash_map[s[i]] = i
            result = max(result, i - start +1)
        return result

test = Solution()

print(test.lengthOfLongestSubstring("bbbbbb"))