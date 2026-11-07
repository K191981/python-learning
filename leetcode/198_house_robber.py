class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0
        prev2 = 0
        for num in nums:
            cur = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = cur
        return prev1
