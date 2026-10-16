class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_num = 0
        ans = len(nums) + 1

        for right in range(len(nums)):
            current_num += nums[right]
            while current_num >= target:
                ans = min(ans, right - left + 1)
                current_num -= nums[left]
                left += 1

        return 0 if ans == len(nums) + 1 else ans
