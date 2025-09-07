class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # the O(n^2) solution
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if nums[i] == nums[j]:
        #            return True
        #return False

        # this one has time complexity O(n), but memory/space complexity of O(n) too
        #hash = {}
        #for thing in nums:
        #    if thing in hash:
        #        return True
        #    else:
        #        hash[thing] = 1
        #return False
    
        # this one is also O(n) time complexity but O(1) space complexity
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False