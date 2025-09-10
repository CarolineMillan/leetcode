class Solution(object):
    def twoSum(self, nums, target):
        # single pass hash approach, O(n) time and space
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            # first check if we've found the answer
            if (target - nums[i]) in hash:
                return (i, hash[target - nums[i]])
            hash[nums[i]] = i