class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in hashmap and hashmap[char] >= left:
                left = hashmap[char] + 1
            hashmap[char] = right
            max_len = max(max_len, right - left + 1)   
        return max_len
