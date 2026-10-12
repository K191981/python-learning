class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {0: 1}
        pre_num = 0
        count = 0
        for num in nums:
            pre_num += num
            count += hashmap.get(pre_num - k, 0)
            hashmap[pre_num] = hashmap.get(pre_num, 0) + 1  
        return count
